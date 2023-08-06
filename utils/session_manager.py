from flask import session
from flask_session import Session
from utils.config import ApplicationConfig

class SessionManager:
    def __init__(self, app):
        app.config.from_object(ApplicationConfig)
        Session(app)

    def create_session(self, user_id):
        session['user_id'] = user_id
        return session.sid

    def destroy_session(self, session_id):
        if session.sid == session_id:
            session.pop('user_id', None)
            return True
        else:
            return False