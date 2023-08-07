from flask import session
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_session import Session
from utils.config import ApplicationConfig

class SessionManager:
    def __init__(self, app):
        app.config.from_object(ApplicationConfig)
        Session(app)

    # def create_session(self, user_id):
    #     session['user_id'] = user_id
    #     return session.sid

    def startSession(self, session_data):
        try:
            if session_data['isVerified']:
                self.startVerifiedSession(session_data)
            else:
                self.startUnverifiedSession(session_data)
        except Exception as ex:
            print(ex)
            return {
                "msg": "cannot start session",
                "errorMsg": "exception"
            }

    def startVerifiedSession(self, session_data):
        session['user'] = session_data
        session['logged_in'] = True
        access_token = create_access_token(identity=session_data)
        refresh_token = create_refresh_token(identity=session_data)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "current_user": session_data,
            "logged_in": True
        }

    # def startUnverifiedSession(self, user):
    #     session['user'] = user
    #     session['logged_in'] = False
    #     msg = Message("Action Required: Confirm your email", sender="noreply@demo.com",
    #                     recipients=[user['email']])
    #     session['verificationCode'] = str(randint(100000, 999999))
    #     msg.body = "We created an account for you. Please confirm your email address." + \
    #         "\nVerification Code : "+session['verificationCode']
    #     mail.send(msg)
    #     return jsonify({
    #         "msg": "check your email!",
    #         "current_user": user,
    #         "logged_in": False
    #     }), 200


    def destroy_session(self, session_id):
        if session.sid == session_id:
            session.pop('user_id', None)
            return True
        else:
            return False