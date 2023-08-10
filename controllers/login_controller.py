from flask import request, jsonify
from services.login_service import LoginService
from dto.login_dto import LoginDTO

class LoginController:
    def __init__(self,app):
        self.login_service = LoginService(app)


    def login(self):
        login_data = LoginDTO(request.json).get_signin_data()
        response = self.login_service.authenticate(login_data)
        return jsonify(response)
    

    def signout(self):
        session_cookie = request.cookies.get('session')
        response = self.login_service.signout(session_cookie)
        return jsonify(response)
    

    def signup(self):
        signup_data = LoginDTO(request.json).get_signup_data()
        session_data = LoginDTO(request.json).get_session_data()
        response = self.login_service.signup_user(signup_data,session_data)
        return jsonify(response)
    

    def sendConfirmationCode(self):
        email = request.json.get('email')
        response = self.login_service.send_confirmation_code(email)
        return jsonify(response)
    
    def verifyEmail(self):
        resquestCode = int(request.json.get('verificationCode'))
        response = self.login_service.verify_email(resquestCode)
        return jsonify(response)
    
    
    def getSessionInfo(self):
        response = self.login_service.getSessionInfo()
        return jsonify(response)