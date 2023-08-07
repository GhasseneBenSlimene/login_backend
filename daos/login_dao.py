from daos import db
from models.user import User

class LoginDAO:
    def __init__(self):
        self.users = db['users']

    def find_by_email(self, email):
        user_doc = self.users.find_one({'email': email})
        if user_doc is None:
            return None
        user_id = str(user_doc['_id'])
        return User( user_doc['name'], user_doc['email'], \
                     user_doc['password'], user_doc['address'], \
                     user_id ,user_doc['isVerified'], user_doc['role'])

    def save(self, signup_data):
        self.users.insert_one(signup_data)
        return User(signup_data["name"], signup_data["email"], \
                    signup_data["password"], signup_data["address"], signup_data["_id"])