from flask import session # Import the session object from Flask
from flask_jwt_extended import create_access_token, create_refresh_token # Import the create_access_token and create_refresh_token functions from Flask-JWT-Extended
from flask_session import Session # Import the Session class from Flask-Session
from utils.config import ApplicationConfig # Import the ApplicationConfig class from the utils.config module
from flask_jwt_extended import JWTManager # Import the JWTManager class from Flask-JWT-Extended
from utils.mail_sender import MailSender # Import the MailSender class from the utils.mail_sender module

class SessionManager:
    def __init__(self, app):
        app.config.from_object(ApplicationConfig) # Load the application configuration from the ApplicationConfig class
        Session(app) # Initialize a new Flask-Session instance with the Flask app
        JWTManager(app) # Initialize a new Flask-JWT-Extended instance with the Flask app
        self.mail_sender=MailSender(app) # Initialize a new MailSender instance with the Flask app

    def startSession(self, session_data):
        try:
            if session_data['isVerified']:
                return self.startVerifiedSession(session_data) # If the user is verified, start a verified session
            else:
                return self.startUnverifiedSession(session_data) # If the user is not verified, start an unverified session
        except Exception as ex:
            print("exception: "+str(ex))
            return {
                "msg": "cannot start session",
                "errorMsg": "exception"
            }
        
    def startVerifiedSession(self, session_data):
        session.pop('verificationCode', None) # Remove the verification code from the session
        session['user'] = session_data # Set the user data in the session
        session['logged_in'] = True # Set the logged_in flag to True
        access_token = create_access_token(identity=session_data) # Create a new access token for the user
        refresh_token = create_refresh_token(identity=session_data) # Create a new refresh token for the user
        return {
            "access_token": access_token,\
            "refresh_token": refresh_token,\
            "logged_in": True
        }
    
    def startUnverifiedSession(self, session_data):
        session['user'] = session_data # Set the user data in the session
        session['logged_in'] = False # Set the logged_in flag to False
        subject = "Action Required: Confirm your email" # Set the subject of the email
        body = "We created an account for you. Please confirm your email address." # Set the body of the email
        self.send_code([session_data['email']], subject, body) # Send the verification code to the user's email
        return {
            "msg": "check your email!",
            "logged_in": False
        }
    
    def start_reset_password_session(self, email, verified=False):
        session["user"] = {
            "email": email, "code_verified": verified
        } # Set the user data in the session for password reset

    def send_code(self, emails, subject, body):
        from random import randint
        session['verificationCode'] = str(randint(100000, 999999)) # Generate a random verification code and store it in the session
        sender = "noreply@demo.com" # Set the sender email address
        recipients = emails # Set the recipient email addresses
        self.mail_sender.set_params(sender, recipients) # Set the sender and recipient email addresses in the MailSender instance

        body += "\nVerification Code : " + session['verificationCode'] # Add the verification code to the email body
        self.mail_sender.send(subject, body) # Send the email with the verification code

    def verify_confirmation_code(self, requestCode):
        session_data = session['user'] # Get the user data from the session
        verificationCode = int(session['verificationCode']) # Get the verification code from the session and convert it to an integer
        if requestCode == verificationCode:
            return session_data # If the provided code matches the verification code, return the user data
        else:
            return None # If the provided code does not match the verification code, return None

    def verify_session(self, session_cookie):
        session_id = session_cookie.split('.')[0] # Get the session ID from the session cookie
        return session.sid == session_id # Check if the session ID matches the current session ID

    def destroy_session(self, session_cookie):
        try:
            if self.verify_session(session_cookie):
                session.pop("logged_in", None) # Remove the logged_in flag from the session
                session.pop("user") # Remove the user data from the session
                session.pop('verificationCode', None) # Remove the verification code from the session
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
    
    def get_session_info(self):
        try:
            if 'user' in session:
                return {
                    "logged_in": session.get('logged_in'),
                    "current_user": session['user']
                } # If the user is logged in, return their user data and the logged_in flag
            else:
                return {
                    "msg": "empty session"
                } # If the user is not logged in, return an error message
        except Exception as ex:
            print(ex)
            return {
                "msg": "cannot get session info",
                "errorMsg": "exception"
            } # If an exception occurs, return an error message
        
    def is_logged_in(self):
        return session.get('logged_in', False)