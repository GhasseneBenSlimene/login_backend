from pymongo import MongoClient

try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mydatabase']
    print('MongoDB connected successfully!')
except Exception as e:
    print('Error connecting to MongoDB:', e)