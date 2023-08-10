from flask import session
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_session import Session
from utils.config import ApplicationConfig
from flask_jwt_extended import JWTManager
from utils.mail_sender import MailSender

class SessionManager:
    def __init__(self, app):
        app.config.from_object(ApplicationConfig)
        Session(app)
        JWTManager(app)
        self.mail_sender=MailSender(app)


    def startSession(self, session_data):
        try:
            if session_data['isVerified']:
                return self.startVerifiedSession(session_data)
            else:
                return self.startUnverifiedSession(session_data)
        except Exception as ex:
            print("exception: "+str(ex))
            return {
                "msg": "cannot start session",
                "errorMsg": "exception"
            }
        

    def startVerifiedSession(self, session_data):
        session.pop('verificationCode', None)
        session['user'] = session_data
        session['logged_in'] = True
        access_token = create_access_token(identity=session_data)
        refresh_token = create_refresh_token(identity=session_data)
        return {
            "access_token": access_token,\
            "refresh_token": refresh_token,\
            "current_user": session_data,\
            "logged_in": True
        }
    

    def startUnverifiedSession(self, session_data):
        session['user'] = session_data
        session['logged_in'] = False
        subject = "Action Required: Confirm your email"
        body = "We created an account for you. Please confirm your email address."
        self.send_code([session_data['email']], subject, body)
        return {
            "msg": "check your email!",
            "current_user": session_data,
            "logged_in": False
        }
    
    def send_code(self, emails, subject, body):
        from random import randint
        session['verificationCode'] = str(randint(100000, 999999))
        sender = "noreply@demo.com"
        recipients = emails
        self.mail_sender.set_params(sender, recipients)

        body += "\nVerification Code : " + session['verificationCode']
        self.mail_sender.send(subject, body)


    def verify_confirmation_code(self, resquestCode):
        session_data = session['user']
        verificationCode = int(session['verificationCode'])
        if resquestCode == verificationCode:
            return session_data
        else:
            return None


    def destroy_session(self, session_cookie):
        try:
            session_id = session_cookie.split('.')[0]
            if session.sid == session_id:
                session.pop("logged_in")
                session.pop("user")
                session.pop('verificationCode', None)
                return {
                    "msg": "user logged out"
                }
            else:
                raise Exception()
        except Exception as ex:
            print("Exception: "+str(ex))
            return {
                "msg": "cannot signout",
                "errorMsg": "exception"
            }
    
    def get_Session_Info(self):
        try:
            if 'user' in session:
                return {
                    "logged_in": session.get('logged_in'),
                    "current_user": session['user']
                }
            else:
                return {
                    "msg": "empty session"
                }
            
        except Exception as ex:
            print(ex)
            return {
                "msg": "cannot get session info",
                "errorMsg": "exception"
            }
