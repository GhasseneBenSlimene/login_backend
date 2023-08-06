from daos.login_dao import LoginDAO
from utils.password_hasher import PasswordHasher
from utils.session_manager import SessionManager

class LoginService:
    def __init__(self, app):
        """
        Initializes the LoginService class with a LoginDAO object, PasswordHasher object, and SessionManager object.

        Parameters:
        app (Flask): The Flask application object.
        """
        self.login_dao = LoginDAO()
        self.password_hasher = PasswordHasher()
        self.session_manager = SessionManager(app)

    def authenticate(self, login_data):
        """
        Authenticates a user with the given login data.

        Parameters:
        login_data (LoginData): The login data object containing the user's email and password.

        Returns:
        dict: A dictionary containing a success flag, message, and session ID (if successful).
        """
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
        """
        Logs out a user with the given session ID.

        Parameters:
        session_id (str): The session ID of the user to log out.

        Returns:
        dict: A dictionary containing a success flag and message.
        """
        if self.session_manager.destroy_session(session_id):
            return {'success': True, 'message': 'Logout successful'}
        else:
            return {'success': False, 'message': 'Invalid session ID'}

    def register_user(self, register_data):
        """
        Registers a new user with the given registration data.

        Parameters:
        register_data (RegisterData): The registration data object containing the user's first name, last name, email, password, and address.

        Returns:
        dict: A dictionary containing a success flag and message.
        """
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