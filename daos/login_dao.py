from daos import db
from models.user import User

class LoginDAO:
    """
    This class represents the data access object for the login functionality.
    It provides methods to find a user by email and to save a new user to the database.
    """

    def __init__(self):
        """
        Initializes a new instance of the LoginDAO class.
        """
        self.users = db['users']

    def find_by_email(self, email):
        """
        Finds a user by email in the database.

        Args:
            email (str): The email of the user to find.

        Returns:
            User: The user object if found, None otherwise.
        """
        user_doc = self.users.find_one({'email': email})
        if user_doc is None:
            return None
        user_id = str(user_doc['_id'])
        return User(user_id, user_doc['first_name'], user_doc['last_name'], user_doc['email'], user_doc['password'], user_doc['address'])

    def save(self, first_name, last_name, email, password, address):
        """
        Saves a new user to the database.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email of the user.
            password (str): The password of the user.
            address (str): The address of the user.

        Returns:
            User: The user object that was saved to the database.
        """
        user_doc = {'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password, 'address': address}
        result = self.users.insert_one(user_doc)
        user_id = str(result.inserted_id)
        return User(user_id, first_name, last_name, email, password, address)