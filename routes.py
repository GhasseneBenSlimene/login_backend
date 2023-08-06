from controllers.login_controller import LoginController
from flask import Flask

app = Flask(__name__)
login_controller = LoginController(app)

@app.route('/user/login', methods=['POST'])
def login():
    """
    This function handles the login request from the user.
    It calls the login method of the LoginController class and returns the result.
    """
    return login_controller.login()

@app.route('/user/logout', methods=['POST'])
def logout():
    """
    This function handles the logout request from the user.
    It calls the logout method of the LoginController class and returns the result.
    """
    return login_controller.logout()

@app.route('/user/register', methods=['POST'])
def register():
    """
    This function handles the register request from the user.
    It calls the register method of the LoginController class and returns the result.
    """
    return login_controller.register()

@app.route('/user/verifyEmail', methods=['POST'])
def verify_email():
    """
    This function handles the verify email request from the user.
    It calls the verify_email method of the LoginController class and returns the result.
    """
    return login_controller.verify_email()

@app.route('/user/sendConfirmationCode', methods=['POST'])
def send_confirmation_code():
    """
    This function handles the send confirmation code request from the user.
    It calls the send_confirmation_code method of the LoginController class and returns the result.
    """
    return login_controller.send_confirmation_code()

@app.route('/test', methods=['GET'])
def test():
    """
    This function is a test route.
    """
    return 'This is a test route!'

if __name__ == '__main__':
    # Run the app in debug mode on host 0.0.0.0 and port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
