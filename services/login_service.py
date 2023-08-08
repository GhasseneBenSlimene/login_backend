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

    def signup_user(self, signup_data, session_data):
        email = signup_data["email"]
        password = signup_data["password"]
        hashed_password = self.password_hasher.hash_password(password)
        signup_data["password"] = hashed_password

        if self.login_dao.find_by_email(email) is not None:
            return {"msg": "Email address already in use"}

        self.login_dao.save(signup_data)
        return self.session_manager.startSession(session_data)

    def send_confirmation_code(self, email):
        try:
            self.session_manager.send_confirmation_code([email])
            return {
                "msg": "check your email!",
                "logged_in": False
            }
        except Exception as ex:
            print(ex)
            return {
                "msg": "cannot send message",
                "errorMsg": "exception"
            }
        
    # add a method that returns the user session