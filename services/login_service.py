from daos.login_dao import LoginDAO
from utils.password_hasher import PasswordHasher
from utils.session_manager import SessionManager

class LoginService:
    def __init__(self, app):
        self.login_dao = LoginDAO()
        self.password_hasher = PasswordHasher()
        self.session_manager = SessionManager(app)

    def authenticate(self, login_data):
        email = login_data.email
        password = login_data.password
        user = self.login_dao.find_by_email(email)

        if user is None:
            return {'success': False, 'message': 'User not found'}

        if not self.password_hasher.check_password(password, user.password):
            return {'success': False, 'message': 'Incorrect password'}

        session_id = self.session_manager.create_session(user.id)
        return {'success': True, 'message': 'Login successful', 'session_id': session_id}

    def logout(self, session_id):
        if self.session_manager.destroy_session(session_id):
            return {'success': True, 'message': 'Logout successful'}
        else:
            return {'success': False, 'message': 'Invalid session ID'}

    def register_user(self, register_data):
        first_name = register_data.first_name
        last_name = register_data.last_name
        email = register_data.email
        password = register_data.password
        address = register_data.address
        hashed_password = self.password_hasher.hash_password(password)

        if self.login_dao.find_by_email(email) is not None:
            return {'success': False, 'message': 'Email already registered'}

        self.login_dao.save(first_name, last_name, email, hashed_password, address)
        return {'success': True, 'message': 'Registration successful'}