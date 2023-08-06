from pymongo import MongoClient

# Connects to the MongoDB database.
try:
    client = MongoClient('mongodb://172.16.238.3:27017/')
    db = client['mydatabase']
    print('MongoDB connected successfully!')
except Exception as e:
    print('Error connecting to MongoDB:', e)