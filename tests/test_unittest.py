import unittest
from unittest.mock import MagicMock, patch
import datetime
from ..FlinkController.dbflink import BatchDatabaseUser
import clickhouse_connect

class TestBatchDatabaseUser(unittest.TestCase):


    @patch('clickhouse_connect.get_client')
    def setUp(self, mock_get_client):
        """Configura l'ambiente di test con un mock del client ClickHouse"""
        self.mock_client = MagicMock()
        mock_get_client.return_value = self.mock_client
        self.db_user = BatchDatabaseUser()
    
    # Il resto dei test rimane invariato

    def test_get_first_user(self):
        """Test per il metodo getFirstUser"""
        # Configura il mock per simulare la risposta del database
        mock_result = MagicMock()
        mock_result.result_rows = [
            (1, 'Mario', 'Rossi', 'M', datetime.date(1990, 5, 15), 'Single', 'Sport'),
            (1, 'Mario', 'Rossi', 'M', datetime.date(1990, 5, 15), 'Single', 'Musica'),
            (1, 'Mario', 'Rossi', 'M', datetime.date(1990, 5, 15), 'Single', 'Cinema')
        ]
        self.mock_client.query.return_value = mock_result
        
        # Esegui la funzione
        result = self.db_user.getFirstUser()
        
        # Verifica la chiamata alla query
        self.mock_client.query.assert_called_once()
        
        # Verifica il risultato
        expected = {
            "id": 1,
            "Nome": "Mario",
            "Cognome": "Rossi",
            "Genere": "M",
            "Data_nascita": datetime.date(1990, 5, 15),
            "Stato_civile": "Single",
            "Interesse1": "Sport",
            "Interesse2": "Musica",
            "Interesse3": "Cinema"
        }
        self.assertEqual(result, expected)
    
    def test_get_activities(self):
        """Test per il metodo getActivities"""
        # Configura il mock per simulare la risposta del database
        mock_result = MagicMock()
        mock_result.result_rows = [
            ('Palestra XYZ', 'Via Roma 123', 'Fitness', 'Palestra ben attrezzata', 150.5),
            ('Bar Sport', 'Via Milano 45', 'Food', 'Bar con specialità locali', 200.3)
        ]
        self.mock_client.query.return_value = mock_result
        
        # Esegui la funzione
        lon, lat = 9.1234, 45.4567
        result = self.db_user.getActivities(lon, lat)
        
        # Verifica la chiamata alla query con i parametri corretti
        self.mock_client.query.assert_called_once()
        call_args = self.mock_client.query.call_args
        self.assertEqual(call_args[1]['parameters'], {'lon': lon, 'lat': lat})
        
        # Verifica il risultato
        expected = [
            ('Palestra XYZ', 'Via Roma 123', 'Fitness', 'Palestra ben attrezzata', 150.5),
            ('Bar Sport', 'Via Milano 45', 'Food', 'Bar con specialità locali', 200.3)
        ]
        self.assertEqual(result, expected)
    
    def test_get_activity_coordinates_found(self):
        """Test per il metodo getActivityCoordinates quando l'attività è trovata"""
        # Configura il mock per simulare la risposta del database
        mock_result = MagicMock()
        mock_result.result_set = [(9.1234, 45.4567)]
        mock_result.first_item = {"lon": 9.1234, "lat": 45.4567}
        self.mock_client.query.return_value = mock_result
        
        # Esegui la funzione
        result = self.db_user.getActivityCoordinates("Palestra XYZ")
        
        # Verifica la chiamata alla query con i parametri corretti
        self.mock_client.query.assert_called_once()
        call_args = self.mock_client.query.call_args
        self.assertEqual(call_args[1]['parameters'], {'nome': 'Palestra XYZ'})
        
        # Verifica il risultato
        expected = {"lon": 9.1234, "lat": 45.4567}
        self.assertEqual(result, expected)
    
    def test_get_activity_coordinates_not_found(self):
        """Test per il metodo getActivityCoordinates quando l'attività non è trovata"""
        # Configura il mock per simulare una risposta vuota
        mock_result = MagicMock()
        mock_result.result_set = []
        self.mock_client.query.return_value = mock_result
        
        # Esegui la funzione
        result = self.db_user.getActivityCoordinates("Attività Inesistente")
        
        # Verifica il risultato per il caso in cui l'attività non esiste
        expected = {"lon": 0, "lat": 0}
        self.assertEqual(result, expected)
    
    def test_get_last_message_coordinates_found(self):
        """Test per il metodo getLastMessageCoordinates quando ci sono messaggi"""
        # Configura il mock per simulare la risposta del database
        mock_result = MagicMock()
        mock_result.result_set = [(9.1234, 45.4567)]
        mock_result.first_item = {"longitude": 9.1234, "latitude": 45.4567}
        self.mock_client.query.return_value = mock_result
        
        # Esegui la funzione
        result = self.db_user.getLastMessageCoordinates()
        
        # Verifica la chiamata alla query
        self.mock_client.query.assert_called_once()
        
        # Verifica il risultato
        expected = {"longitude": 9.1234, "latitude": 45.4567}
        self.assertEqual(result, expected)
    
    def test_get_last_message_coordinates_not_found(self):
        """Test per il metodo getLastMessageCoordinates quando non ci sono messaggi"""
        # Configura il mock per simulare una risposta vuota
        mock_result = MagicMock()
        mock_result.result_set = []
        self.mock_client.query.return_value = mock_result
        
        # Esegui la funzione
        result = self.db_user.getLastMessageCoordinates()
        
        # Verifica il risultato per il caso in cui non ci sono messaggi
        expected = {"longitude": 0, "latitude": 0}
        self.assertEqual(result, expected)
        

class TestBatchDatabaseUserIntegration(unittest.TestCase):
    """Test di integrazione che richiede un server ClickHouse reale"""
    
    @unittest.skip("Test di integrazione che richiede un server ClickHouse")
    def setUp(self):
        """Configura la connessione al database reale"""
        self.db_user = BatchDatabaseUser()
        # Qui si potrebbe configurare un database di test con dati noti
    
    @unittest.skip("Test di integrazione che richiede un server ClickHouse")
    def test_integration_get_first_user(self):
        """Test di integrazione per getFirstUser"""
        result = self.db_user.getFirstUser()
        self.assertIsInstance(result, dict)
        self.assertIn("id", result)
        self.assertIn("Nome", result)
        # Altre verifiche sui dati reali
    
    @unittest.skip("Test di integrazione che richiede un server ClickHouse")
    def test_integration_get_activities(self):
        """Test di integrazione per getActivities"""
        # Coordinate del centro di Milano
        lon, lat = 9.1900, 45.4642
        result = self.db_user.getActivities(lon, lat)
        self.assertIsInstance(result, list)
        # Altre verifiche sui dati reali

