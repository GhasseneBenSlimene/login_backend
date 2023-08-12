from daos import db # Import the db object from the daos module
from dto.login_dto import LoginDTO # Import the LoginDTO class from the login_dto module
from models.user import User # Import the User class from the models module

class LoginDAO:
    def __init__(self):
        self.users = db['users'] # Set the users collection in the db object as an instance variable

    def find_by_email(self, email):
        user_doc = self.users.find_one({'email': email}) # Find a user document in the users collection with the given email
        if user_doc is None: # If no user document is found, return None
            return None
        user_id = str(user_doc['_id']) # Get the user ID from the user document and convert it to a string
        return User( user_doc['name'], user_doc['email'], \
                     user_doc['password'], user_doc['address'], \
                     user_id ,user_doc['isVerified'], user_doc['role']) # Create a new User instance with the user document data and return it

    def save(self, signup_data):
        self.users.insert_one(signup_data) # Insert the signup data into the users collection
        return User(signup_data["name"], signup_data["email"], \
                    signup_data["password"], signup_data["address"], signup_data["_id"]) # Create a new User instance with the signup data and return it
    
    def find_session_by_email(self, email):
        user_doc = self.find_by_email(email) # Find a user document with the given email
        if user_doc is None: # If no user document is found, return None
            return None
        user_data = LoginDTO.from_user(user_doc) # Create a new LoginDTO instance with the user document data
        session_data = user_data.get_session_data() # Get the session data from the LoginDTO instance
        return session_data # Return the session data

    def update(self, email, update_data):
        user_doc = self.users.find_one({'email': email}) # Find a user document with the given email
        if user_doc is None: # If no user document is found, return None
            return None
        self.users.update_one({'email': email}, {'$set': update_data}) # Update the user document with the given email with the update data
        updated_user_doc = self.users.find_one({'email': email}) # Find the updated user document with the given email
        user_id = str(updated_user_doc['_id']) # Get the user ID from the updated user document and convert it to a string
        return User(updated_user_doc['name'], updated_user_doc['email'], \
                    updated_user_doc['password'], updated_user_doc['address'], \
                    user_id, updated_user_doc['isVerified'], updated_user_doc['role']) # Create a new User instance with the updated user document data and return it