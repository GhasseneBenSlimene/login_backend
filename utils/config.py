from datetime import timedelta
from dotenv import load_dotenv
import os
import redis

load_dotenv()

# Define the ApplicationConfig class
class ApplicationConfig:
    # Set the SECRET_KEY attribute to the value of the SECRET_KEY environment variable
    SECRET_KEY = os.environ["SECRET_KEY"]

    # Set the session type to "redis"
    SESSION_TYPE = "redis"
    # Set SESSION_PERMANENT to False
    SESSION_PERMANENT = False
    # Set SESSION_USE_SIGNER to True
    SESSION_USE_SIGNER = True
    # Set SESSION_REDIS to a Redis instance created from the URL "redis://172.16.238.4:6379"
    SESSION_REDIS = redis.from_url("redis://172.16.238.4:6379")
    # Set SESSION_REDIS to a Redis instance created from the URL "redis://127.0.0.1:6379"
    # SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")

    # Set the MAIL_SERVER attribute to 'smtp.gmail.com'
    MAIL_SERVER = 'smtp.gmail.com'
    # Set the MAIL_PORT attribute to 587
    MAIL_PORT = 587
    # Set the MAIL_USERNAME attribute to the value of the MAIL_USERNAME environment variable
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # Set the MAIL_PASSWORD attribute to the value of the MAIL_PASSWORD environment variable
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # Set the MAIL_USE_TLS attribute to True
    MAIL_USE_TLS = True
    # Set the MAIL_USE_SSL attribute to False
    MAIL_USE_SSL = False

    # Set the JWT_SECRET_KEY attribute to the value of the SECRET_KEY environment variable
    JWT_SECRET_KEY = os.environ["SECRET_KEY"]
    # Set the JWT_ACCESS_TOKEN_EXPIRES attribute to 1 hour
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    # Set the JWT_REFRESH_TOKEN_EXPIRES attribute to 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=1)