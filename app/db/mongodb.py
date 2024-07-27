import pymongo

class MongoBDClient():
    _instance = None
    
    def __new__(cls, uri, db_name):
        if cls._instance == None :
            cls._instance = super(MongoBDClient, cls).__new__(cls)
            cls._instance._initialize(uri, db_name)
        return cls._instance
            
    def _initialize(self, uri, db_name) -> None:
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]
    
    def get_db(self):
        return self.db