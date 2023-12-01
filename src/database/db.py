from pymongo import MongoClient
from os import environ


mongo_uri = environ.get('MONGO_URI', 'mongodb://localhost:27017/')


db_name = environ.get('DB_NAME', 'test_db_traduzo')

client = MongoClient(mongo_uri)
db = client[db_name]
