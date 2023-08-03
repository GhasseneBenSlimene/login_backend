class User:
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.email}>'