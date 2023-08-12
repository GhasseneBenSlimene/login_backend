Flask Web Application:
This is a Flask web application that provides user authentication and registration functionality. The application uses a LoginController object to handle the actual authentication and registration logic, while the Flask routes simply call the appropriate methods of the LoginController object.

Installation:
To install the application, you will need to have Python 3 and pip installed on your system. Once you have these dependencies installed, you can install the required Python packages by running the following command:

pip install -r requirements.txt

Usage:
To run the application, you can execute the following command:

python routes.py

Alternatively, you can use Docker Compose to start the app. To do this, make sure you have Docker and Docker Compose installed on your system, then run the following command:

docker compose up

This will start the Flask development server inside a Docker container, which you can access by navigating to http://localhost:5000 in your web browser.
