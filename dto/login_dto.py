class LoginDTO:
    def __init__(self, data):
        self.name = data.get('firstName')+" "+data.get('lastName')
        self.email = data.get('email')
        self.password = data.get('password')
        self.address = data.get('address')

    def get_signin_data(self):
        return {
            "email": self.email,
            "password": self.password
        }
    
    def get_signup_data(self):
        import uuid
        return {
            "_id": uuid.uuid4().hex,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "address": self.address,
            "isVerified": False,
            "role": "user"
        }
    
    def get_session_data(self):
        import uuid
        return {
            "_id": uuid.uuid4().hex,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "isVerified": False,
            "role": "user"
        }
    
    @staticmethod
    def from_user(user):
        data = {
            "name": user.name,
            "email": user.email,
            "password": user.password,
            "address": user.address
        }
        return LoginDTO(data)