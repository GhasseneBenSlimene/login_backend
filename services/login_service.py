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
            
            new_session = self.session_manager.startSession(session_data)
            return new_session
    
        except Exception as ex:
            print(ex)
            return {
                "msg": "cannot login",
                "errorMsg": "exception"
            }
        

    def signout(self, session_cookie):
        return self.session_manager.destroy_session(session_cookie)
    

    def signup_user(self, signup_data, session_data):
        email = signup_data["email"]
        password = signup_data["password"]
        hashed_password = self.password_hasher.hash_password(password)
        signup_data["password"] = hashed_password

        if self.login_dao.find_by_email(email) is not None:
            return {"msg": "Email address already in use"}

        self.login_dao.save(signup_data)

        new_session = self.session_manager.startSession(session_data)
        return new_session
    

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
    
    
    def verify_email(self, resquestCode):
        try:
            session_data = self.session_manager.verify_confirmation_code(resquestCode)
            if session_data is not None:
                email = session_data['email']
                update_data = {"isVerified": True}
                if (self.login_dao.update(email,update_data)):
                    session_data["isVerified"]=True
                    new_session = self.session_manager.startSession(session_data)
                    return new_session
                else:
                    {
                        "msg": "verification failed"
                    }
            else:
                return {
                "msg": "not equal"
                }
        except Exception as ex:
            print(ex)
            return {
                "msg": "cannot verify",
                "errorMsg": "exception"
            }