from flask import session
from flask_session import Session
from utils.config import ApplicationConfig

class SessionManager:
    """
    A class used to manage user sessions.

    Attributes
    ----------
    app : Flask
        The Flask application instance.

    Methods
    -------
    create_session(user_id)
        Creates a new session for the given user ID.
    destroy_session(session_id)
        Destroys the session with the given session ID.
    """

    def __init__(self, app):
        """
        Initializes the SessionManager instance.

        Parameters
        ----------
        app : Flask
            The Flask application instance.
        """
        app.config.from_object(ApplicationConfig)
        Session(app)

    def create_session(self, user_id):
        """
        Creates a new session for the given user ID.

        Parameters
        ----------
        user_id : str
            The ID of the user to create a session for.

        Returns
        -------
        str
            The ID of the newly created session.
        """
        session['user_id'] = user_id
        return session.sid

    def destroy_session(self, session_id):
        """
        Destroys the session with the given session ID.

        Parameters
        ----------
        session_id : str
            The ID of the session to destroy.

        Returns
        -------
        bool
            True if the session was successfully destroyed, False otherwise.
        """
        if session.sid == session_id:
            session.pop('user_id', None)
            return True
        else:
            return False