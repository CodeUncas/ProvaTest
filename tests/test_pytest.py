import sys
import json
import pytest
from unittest.mock import patch, Mock, call
from datetime import datetime
from confluent_kafka import Producer

# Mock delle librerie esterne per isolare i test
@pytest.fixture
def mock_dependencies():
    mocks = {
        'Producer': patch('confluent_kafka.Producer'),
        'nx': patch('networkx.shortest_path'),
        'ox': patch('osmnx.graph_from_point'),
        'time': patch('time.sleep'),
        'datetime': patch('datetime.datetime')
    }
    
    for name, patcher in mocks.items():
        mocks[name] = patcher.start()
    
    # Configurazione dei mock
    mocks['Producer'].return_value = Mock()
    mocks['ox'].return_value = Mock()
    
    # Simula il comportamento di datetime.now()
    mock_now = Mock()
    mock_now.strftime.return_value = "2025-02-28 10:15:30"
    mocks['datetime'].now.return_value = mock_now
    
    yield mocks
    
    # Ferma tutti i mock
    for patcher in mocks.values():
        try:
            patcher.stop()
        except:
            pass

@pytest.fixture
def sample_route():
    """Genera un percorso di test con coordinate"""
    return [
        (45.39, 11.87),  # Punto iniziale
        (45.395, 11.875),  # Punto intermedio
        (45.40, 11.88),   # Punto finale
    ]

def test_generate_positions(mock_dependencies, monkeypatch, sample_route):
    """Test della funzione generate_positions"""
    # Configurazione del test
    mock_producer = mock_dependencies['Producer'].return_value
    
    # Import il modulo dopo aver configurato i mock
    with patch.object(sys, 'modules', sys.modules.copy()):
        # Importazione isolata per evitare esecuzioni globali
        import importlib.util
        spec = importlib.util.spec_from_file_location("simulatePosition", "./simulatePosition.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Sostituisci la funzione generate_positions per testarla separatamente
        with patch('builtins.print') as mock_print:
            # Esegui la funzione di test
            module.generate_positions(sample_route, 15, 1)  # Usa intervallo=1 per velocizzare il test
            
            # Verifica le chiamate al producer
            assert mock_producer.produce.call_count > 0
            assert mock_producer.flush.call_count > 0
            
            # Verifica che i dati siano nel formato corretto
            call_args = mock_producer.produce.call_args_list[0][1]
            value = json.loads(call_args['value'].decode('utf-8'))
            
            # Verifica i campi del messaggio
            assert 'id' in value
            assert 'latitude' in value
            assert 'longitude' in value
            assert 'received_at' in value
            
            # Verifica che le coordinate siano nel range corretto
            assert 45.39 <= value['latitude'] <= 45.40
            assert 11.87 <= value['longitude'] <= 11.88

def test_error_handling(mock_dependencies, monkeypatch):
    """Test della gestione degli errori"""
    # Configura il producer per generare un'eccezione
    mock_producer = mock_dependencies['Producer'].return_value
    mock_producer.produce.side_effect = Exception("Kafka connection error")
    
    with patch('builtins.print') as mock_print:
        with patch.object(sys, 'modules', sys.modules.copy()):
            try:
                # Import del modulo per forzare l'esecuzione
                import importlib.util
                spec = importlib.util.spec_from_file_location("simulatePosition", "./simulatePosition.py")
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
            except:
                pass
            
            # Verifica che l'errore sia stato catturato e stampato
            error_message_call = [call for call in mock_print.call_args_list 
                                 if "Error sending data" in str(call)]
            assert len(error_message_call) > 0