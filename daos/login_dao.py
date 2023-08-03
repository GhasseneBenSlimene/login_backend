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
        return User(user_id, user_doc['email'], user_doc['password'])

    def save(self, email, password):
        user_doc = {'email': email, 'password': password}
        result = self.users.insert_one(user_doc)
        user_id = str(result.inserted_id)
        return User(user_id, email, password)