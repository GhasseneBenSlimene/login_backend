class User:
    def __init__(self, id, first_name, last_name, email, password, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.address = address

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name} ({self.email})>'