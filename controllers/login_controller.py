from flask import request, jsonify # Import the request and jsonify functions from the flask module
from services.login_service import LoginService # Import the LoginService class from the login_service module
from dto.login_dto import LoginDTO # Import the LoginDTO class from the login_dto module

class LoginController:
    def __init__(self,app):
        self.login_service = LoginService(app) # Create a new LoginService instance and pass in the Flask app instance

    def login(self):
        login_data = LoginDTO(request.json).get_signin_data() # Create a new LoginDTO instance and pass in the request JSON data, then get the signin data
        response = self.login_service.authenticate(login_data) # Call the authenticate method of the LoginService instance and pass in the signin data
        return jsonify(response) # Return the response as a JSON object

    def signout(self):
        session_cookie = request.cookies.get('session') # Get the session cookie from the request
        response = self.login_service.signout(session_cookie) # Call the signout method of the LoginService instance and pass in the session cookie
        return jsonify(response) # Return the response as a JSON object

    def signup(self):
        signup_data = LoginDTO(request.json).get_signup_data() # Create a new LoginDTO instance and pass in the request JSON data, then get the signup data
        session_data = LoginDTO(request.json).get_session_data() # Create a new LoginDTO instance and pass in the request JSON data, then get the session data
        response = self.login_service.signup_user(signup_data,session_data) # Call the signup_user method of the LoginService instance and pass in the signup and session data
        return jsonify(response) # Return the response as a JSON object

    def sendConfirmationCode(self):
        email = request.json.get('email') # Get the email from the request JSON data
        response = self.login_service.send_confirmation_code(email) # Call the send_confirmation_code method of the LoginService instance and pass in the email
        return jsonify(response) # Return the response as a JSON object

    def verifyEmail(self):
        requestCode = int(request.json.get('verificationCode')) # Get the verification code from the request JSON data and convert it to an integer
        response = self.login_service.verify_email(requestCode) # Call the verify_email method of the LoginService instance and pass in the verification code
        return jsonify(response) # Return the response as a JSON object

    def getSessionInfo(self):
        response = self.login_service.get_session_info() # Call the get_session_info method of the LoginService instance
        return jsonify(response) # Return the response as a JSON object

    def resetPasswordStep1(self):
        email = request.json.get("email") # Get the email from the request JSON data
        response = self.login_service.reset_password_step1(email) # Call the reset_password_step1 method of the LoginService instance and pass in the email
        return jsonify(response) # Return the response as a JSON object

    def resetPasswordStep2(self):
        requestCode = int(request.json.get('verificationCode')) # Get the verification code from the request JSON data and convert it to an integer
        response = self.login_service.reset_password_step2(requestCode) # Call the reset_password_step2 method of the LoginService instance and pass in the verification code
        return jsonify(response) # Return the response as a JSON object

    def resetPasswordStep3(self):
        password = request.json.get("password") # Get the new password from the request JSON data
        session_cookie = request.cookies.get('session') # Get the session cookie from the request
        response = self.login_service.reset_password_step3(password, session_cookie) # Call the reset_password_step3 method of the LoginService instance and pass in the new password and session cookie
        return jsonify(response) # Return the response as a JSON object