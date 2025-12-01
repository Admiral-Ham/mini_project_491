from dotenv import load_dotenv, find_dotenv
import os
#import pprint
from pymongo import MongoClient


load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://alberts_db_user:{password}@testdatabase.1axf3iy.mongodb.net/?appName=testDatabase"

connection_string_2 = "mongodb+srv://technicsolutions:technicsolutions491a@technicsolutions.kpxzyep.mongodb.net/?retryWrites=true&w=majority&appName=TechnicSolutions"


#MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME") 

db_name_1 = "budgettracker"
                     
client = MongoClient(connection_string_2)
db = client[db_name_1]