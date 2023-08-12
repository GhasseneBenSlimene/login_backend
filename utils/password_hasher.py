import bcrypt # Import the bcrypt module

class PasswordHasher:
    def __init__(self):
        self.salt = bcrypt.gensalt() # Generate a new salt using bcrypt's gensalt method and set it as an instance attribute

    def hash_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), self.salt) # Hash the provided password using bcrypt's hashpw method and the instance's salt attribute
        return hashed_password.decode('utf-8') # Return the hashed password as a UTF-8 encoded string

    def check_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')) # Check if the provided password matches the provided hashed password using bcrypt's checkpw method