from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pathlib import Path

import configparser
BASE_DIR = Path(__file__).resolve().parent.parent.parent

config = configparser.ConfigParser()
config.read(BASE_DIR / 'config.ini') 

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')

# connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)

uri = f"mongodb+srv://{mongo_user}:{mongodb_pass}@cluster0.z5qyfaa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.test
