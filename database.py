import pymongo

__author__ = 'jslvtr'


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    # finds data and returns a pymongo.cursor.cursor

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
    # gets the first element referring to the cursor
    # then returns the json object that stored in the db directly
