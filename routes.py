from controllers.login_controller import LoginController # Import the LoginController class from the login_controller module
from flask import Flask # Import the Flask class from the flask module

app = Flask(__name__) # Create a new Flask app instance
login_controller = LoginController(app) # Create a new LoginController instance and pass in the Flask app instance

@app.route('/test', methods=['GET']) # Define a new route for the /test endpoint
def test():
    return 'This is a test route!' # Return a string when the route is accessed

@app.route('/user/login', methods=['POST']) # Define a new route for the /user/login endpoint
def login():
    return login_controller.login() # Call the login method of the LoginController instance when the route is accessed

@app.route('/user/signout', methods=['GET']) # Define a new route for the /user/signout endpoint
def logout():
    return login_controller.signout() # Call the signout method of the LoginController instance when the route is accessed

@app.route('/user/signup', methods=['POST']) # Define a new route for the /user/signup endpoint
def register():
    return login_controller.signup() # Call the signup method of the LoginController instance when the route is accessed

@app.route("/user/sendConfirmationCode", methods=['POST']) # Define a new route for the /user/sendConfirmationCode endpoint
def sendConfirmationCode():
    return login_controller.sendConfirmationCode() # Call the sendConfirmationCode method of the LoginController instance when the route is accessed

@app.route('/user/verifyEmail', methods=['POST']) # Define a new route for the /user/verifyEmail endpoint
def verifyEmail():
    return login_controller.verifyEmail() # Call the verifyEmail method of the LoginController instance when the route is accessed

@app.route('/@me', methods=['GET']) # Define a new route for the /@me endpoint
def getSessionInfo():
    return login_controller.getSessionInfo() # Call the getSessionInfo method of the LoginController instance when the route is accessed

@app.route('/resetPasswordStep1', methods=['POST']) # Define a new route for the /resetPasswordStep1 endpoint
def resetPasswordStep1():
    return login_controller.resetPasswordStep1() # Call the resetPasswordStep1 method of the LoginController instance when the route is accessed

@app.route('/resetPasswordStep2', methods=['POST']) # Define a new route for the /resetPasswordStep2 endpoint
def resetPasswordStep2():
    return login_controller.resetPasswordStep2() # Call the resetPasswordStep2 method of the LoginController instance when the route is accessed

@app.route('/resetPasswordStep3', methods=['POST']) # Define a new route for the /resetPasswordStep3 endpoint
def resetPasswordStep3():
    return login_controller.resetPasswordStep3() # Call the resetPasswordStep3 method of the LoginController instance when the route is accessed

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000) # Start the Flask app on port 5000 and listen for incoming requests