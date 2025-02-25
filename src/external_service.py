class DatabaseService:
    def get_user_data(self, user_id):
        # Simula una chiamata al database
        # In un caso reale, questa funzione si connetterebbe a un database

        if user_id is None:
            raise NotImplementedError("Real database connection not implemented")

class EmailService:
    def send_email(self, to_address, subject, body):
        # Simula l'invio di una email
        # In un caso reale, questa funzione invierebbe una vera email
        raise NotImplementedError("Real email sending not implemented")

class UserManager:
    def __init__(self, db_service, email_service):
        self.db_service = db_service
        self.email_service = email_service
    
    def notify_user(self, user_id):
        user_data = self.db_service.get_user_data(user_id)
        if user_data:
            self.email_service.send_email(
                user_data['email'],
                "Notification",
                f"Hello {user_data['name']}!"
            )
            return True
        return False
