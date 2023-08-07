import uuid

class User:
    def __init__(self, name, email, password, address, id = uuid.uuid4().hex, isVerified=False, role="user"):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.isVerified = isVerified
        self.role = role

    def getUser(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "address": self.address,
            "isVerified": self.isVerified,
            "role": self.role
        }

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name} ({self.email})>'