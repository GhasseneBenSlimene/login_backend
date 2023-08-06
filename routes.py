from controllers.login_controller import LoginController
from flask import Flask

app = Flask(__name__)
login_controller = LoginController(app)

@app.route('/user/login', methods=['POST'])
def login():
    return login_controller.login()

@app.route('/user/logout', methods=['POST'])
def logout():
    return login_controller.logout()

@app.route('/user/register', methods=['POST'])
def register():
    return login_controller.register()

@app.route('/test', methods=['GET'])
def test():
    return 'This is a test route!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)