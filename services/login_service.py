from daos.login_dao import LoginDAO
from utils.password_hasher import PasswordHasher
from utils.session_manager import SessionManager

class LoginService:
    def __init__(self, app):
        self.login_dao = LoginDAO()
        self.password_hasher = PasswordHasher()
        self.session_manager = SessionManager(app)

    def authenticate(self, login_data):
        try:
            email = login_data["email"]
            password = login_data["password"]
            user = self.login_dao.find_by_email(email)

            if user is None:
                return {
                    "msg": "Invalid login credentials"
                }

            if not self.password_hasher.check_password(password, user.password):
                return {
                    "msg": "Invalid login credentials"
                }
            
            session_data = self.login_dao.find_session_by_email(email)
            
            session = self.session_manager.startSession(session_data)
            return session
    
        except Exception as ex:
            print(ex)
            return {
                "msg": "cannot login",
                "errorMsg": "exception"
            }

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

        session = self.session_manager.startSession(session_data)
        return session

    def send_confirmation_code(self, email):
        try:
            session_data = self.login_dao.find_session_by_email(email)
            if session_data is None:
                raise ValueError("Email not found in database")
            self.session_manager.send_confirmation_code([email])
            return {
                "msg": "check your email!",
                "current_user": session_data,
                "logged_in": False
            }
        except ValueError as ex:
            print("Exception: "+ str(ex))
            return {
                "msg": "cannot send message",
                "errorMsg": str(ex)
            }
        except Exception as ex:
            print("Exception: "+ str(ex))
            return {
                "msg": "cannot send message",
                "errorMsg": "exception"
            }