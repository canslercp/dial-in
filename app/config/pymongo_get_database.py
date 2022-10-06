from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def get_database():
  # connect python to mongodb using pymongo and env variable
  CONNECTION_STRING = getenv("DB_URL")

  # create a connection using MongoClient
  client = MongoClient(CONNECTION_STRING)

  # create the database 
  return client['dial_in']

# allows many files to reuse the function get_database()
if __name__ == "__main__":
    # get the database
    dbname = get_database()