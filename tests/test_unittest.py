# import unittest
# from unittest.mock import Mock, patch
# from src.external_service import UserManager, DatabaseService, EmailService

# class TestUserManager(unittest.TestCase):
    # def setUp(self):
    #     self.db_service = Mock(spec=DatabaseService)
    #     self.email_service = Mock(spec=EmailService)
    #     self.user_manager = UserManager(self.db_service, self.email_service)

    # def test_notify_user_success(self):
    #     # Configura il mock per simulare un utente esistente
    #     self.db_service.get_user_data.return_value = {
    #         'email': 'test@example.com',
    #         'name': 'Test User'
    #     }

    #     # Chiama il metodo da testare
    #     result = self.user_manager.notify_user(1)

    #     # Verifica che il risultato sia True
    #     self.assertTrue(result)
        
    #     # Verifica che i mock siano stati chiamati correttamente
    #     self.db_service.get_user_data.assert_called_once_with(1)
    #     self.email_service.send_email.assert_called_once_with(
    #         'test@example.com',
    #         'Notification',
    #         'Hello Test User!'
    #     )

    # def test_notify_user_not_found(self):
    #     # Configura il mock per simulare un utente non esistente
    #     self.db_service.get_user_data.return_value = None

    #     # Chiama il metodo da testare
    #     result = self.user_manager.notify_user(1)

    #     # Verifica che il risultato sia False
    #     self.assertFalse(result)
        
    #     # Verifica che get_user_data sia stato chiamato ma non send_email
    #     self.db_service.get_user_data.assert_called_once_with(1)
    #     self.email_service.send_email.assert_not_called()

    # @patch('src.external_service.DatabaseService')
    # @patch('src.external_service.EmailService')
    # def test_notify_user_with_patch(self, mock_email_service, mock_db_service):
    #     # Esempio di uso del decoratore patch
    #     mock_db_service.get_user_data.return_value = {
    #         'email': 'test@example.com',
    #         'name': 'Test User'
    #     }
        
    #     user_manager = UserManager(mock_db_service, mock_email_service)
    #     result = user_manager.notify_user(1)
        
    #     self.assertTrue(result)


