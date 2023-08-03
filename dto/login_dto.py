class LoginDTO:
    def __init__(self, data):
        self.email = data.get('email')
        self.password = data.get('password')