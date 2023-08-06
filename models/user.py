class User:
    """
    A class representing a user.

    Attributes:
    -----------
    id : int
        The unique identifier of the user.
    first_name : str
        The first name of the user.
    last_name : str
        The last name of the user.
    email : str
        The email address of the user.
    password : str
        The password of the user.
    address : str
        The address of the user.

    Methods:
    --------
    __repr__() -> str
        Returns a string representation of the user object.
    """

    def __init__(self, id, first_name, last_name, email, password, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.address = address

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name} ({self.email})>'