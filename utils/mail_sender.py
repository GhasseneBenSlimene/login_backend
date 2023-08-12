from flask_mail import Mail, Message # Import the Mail and Message classes from the flask_mail module

class MailSender:
    def __init__(self, app):
        self.mail = Mail(app) # Initialize a new Mail instance with the Flask app

    def set_params(self, sender, recipients):
        self.sender = sender # Set the sender attribute to the provided sender email address
        self.recipients = recipients # Set the recipients attribute to the provided list of recipient email addresses

    def send(self, subject, body):
        msg = Message(subject, sender=self.sender, recipients=self.recipients) # Create a new Message instance with the provided subject, sender, and recipients
        msg.body = body # Set the body of the message to the provided body text
        self.mail.send(msg) # Send the message using the Mail instance's send method