from controllers.login_controller import LoginController
from flask import Flask

app = Flask(__name__)
login_controller = LoginController(app)

@app.route('/user/login', methods=['POST'])
def login():
    return login_controller.login()

@app.route('/user/signout', methods=['GET'])
def logout():
    return login_controller.signout()

@app.route('/user/signup', methods=['POST'])
def register():
    return login_controller.signup()

@app.route("/user/sendConfirmationCode", methods=['POST'])
def sendConfirmationCode():
    return login_controller.sendConfirmationCode()

@app.route('/user/verifyEmail', methods=['POST'])
def verifyEmail():
    return login_controller.verifyEmail()

@app.route('/test', methods=['GET'])
def test():
    return 'This is a test route!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)