from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import configparser

config = configparser.ConfigParser()
config.read('config.ini') #I put my original config file not in this folder, so the path to the file was different

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')

# connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)

uri = f"mongodb+srv://{mongo_user}:{mongodb_pass}@cluster0.z5qyfaa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.test
