from flask import request, jsonify
from services.login_service import LoginService
from dto.login_dto import LoginDTO

class LoginController:
    def __init__(self,app):
        self.login_service = LoginService(app)

    def login(self):
        login_data = LoginDTO(request.json)
        response = self.login_service.authenticate(login_data)
        return jsonify(response)

    def logout(self):
        session_cookie = request.cookies.get('session')
        session_id=session_id = session_cookie.split('.')[0]
        response = self.login_service.logout(session_id)
        return jsonify(response)

    def register(self):
        register_data = LoginDTO(request.json)
        response = self.login_service.register_user(register_data)
        return jsonify(response)