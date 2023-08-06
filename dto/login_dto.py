class LoginDTO:
    """
    Data Transfer Object for Login information.
    """
    def __init__(self, data):
        # Initialize the LoginDTO object with the given data.
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.email = data.get('email')
        self.password = data.get('password')
        self.address = data.get('address')