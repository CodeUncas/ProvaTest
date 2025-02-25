import pytest 
from unittest.mock import Mock,patch
from src.external_service import UserManager, DatabaseService, EmailService

@pytest.fixture
def mocker():
    return Mock()

def test_notify_user_success(mocker):
    # Crea i mock usando pytest-mock
    mock_db = mocker.Mock(spec=DatabaseService)
    mock_email = mocker.Mock(spec=EmailService)
    
    # Configura il comportamento del mock
    mock_db.get_user_data.return_value = {
        'email': 'test@example.com',
        'name': 'Test User'
    }
    
    # Crea l'istanza da testare
    user_manager = UserManager(mock_db, mock_email)
    
    # Esegui il test
    result = user_manager.notify_user(1)
    
    # Verifica i risultati
    assert result is True
    mock_db.get_user_data.assert_called_once_with(1)
    mock_email.send_email.assert_called_once_with(
        'test@example.com',
        'Notification',
        'Hello Test User!'
    )

def test_notify_user_not_found(mocker):
    # Crea i mock usando pytest-mock
    mock_db = mocker.Mock(spec=DatabaseService)
    mock_email = mocker.Mock(spec=EmailService)
    
    # Configura il mock per simulare utente non trovato
    mock_db.get_user_data.return_value = None
    
    user_manager = UserManager(mock_db, mock_email)
    result = user_manager.notify_user(1)
    
    assert result is False
    mock_db.get_user_data.assert_called_once_with(1)
    mock_email.send_email.assert_not_called()





    