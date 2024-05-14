from pymongo import MongoClient;
from pymongo.errors import PyMongoError;

try:
    # Create Connection
    client = MongoClient('mongodb://localhost:27017')
    # Select Database
    MyDB = client['db'];
    # collection
    collection = MyDB['collectionname'];

except PyMongoError as e:
    print(e) 
