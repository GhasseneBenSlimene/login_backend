from dotenv import load_dotenv
import os
import redis

load_dotenv()

class ApplicationConfig:
    """
    This class contains the configuration settings for the Flask application.
    """

    # The secret key used for signing cookies and other secure tokens.
    SECRET_KEY = os.environ["SECRET_KEY"]

    # The type of session interface to use.
    SESSION_TYPE = "redis"

    # Whether the session should be permanent or not.
    SESSION_PERMANENT = False

    # Whether to use a signer for the session cookie.
    SESSION_USE_SIGNER = True

    # The Redis instance to use for storing session data.
    SESSION_REDIS = redis.from_url("redis://172.16.238.4:6379")    

    # Note: You may need to modify the Redis URL to match your own environment.
