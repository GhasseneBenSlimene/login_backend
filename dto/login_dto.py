class LoginDTO:
    def __init__(self, data):
        if "firstName" in data and "firstName" in data: # Check if the data contains both 'firstName' and 'lastName' keys
            self.name = data.get('firstName') + " " + data.get('lastName') # If so, set the name attribute to the concatenation of the 'firstName' and 'lastName' values
            self.email = data.get('email') # Set the email attribute to the 'email' value
            self.password = data.get('password') # Set the password attribute to the 'password' value
            self.address = data.get('address') # Set the address attribute to the 'address' value
            self.isVerified = data.get('isVerified', False) # Set the isVerified attribute to the 'isVerified' value, or False if it doesn't exist
            self.role = data.get('role', 'user') # Set the role attribute to the 'role' value, or 'user' if it doesn't exist
        else:
            self.name = data.get('name') # If the data doesn't contain both 'firstName' and 'lastName' keys, set the name attribute to the 'name' value
            self.email = data.get('email') # Set the email attribute to the 'email' value
            self.password = data.get('password') # Set the password attribute to the 'password' value
            self.address = data.get('address') # Set the address attribute to the 'address' value
            self.isVerified = data.get('isVerified', False) # Set the isVerified attribute to the 'isVerified' value, or False if it doesn't exist
            self.role = data.get('role', 'user') # Set the role attribute to the 'role' value, or 'user' if it doesn't exist

    def get_signin_data(self):
        return {
            "email": self.email,
            "password": self.password
        }
    
    def get_signup_data(self):
        import uuid
        return {
            "_id": uuid.uuid4().hex, # Generate a new UUID and set it as the '_id' value
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "address": self.address,
            "isVerified": self.isVerified,
            "role": self.role
        }
    
    def get_session_data(self):
        import uuid
        return {
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "isVerified": self.isVerified,
            "role": self.role
        }
    
    @staticmethod
    def from_user(user):
        data = {
            "id": user.id, # Set the 'id' value to the user's ID
            "name": user.name,
            "email": user.email,
            "password": user.password,
            "address": user.address,
            "isVerified": user.isVerified,
            "role": user.role
        }
        return LoginDTO(data) # Create a new LoginDTO instance with the data and return it