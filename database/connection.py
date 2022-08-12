from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

class Connection:
    """A class for creating database connection"""
    def __init__(self):
        """Constructor"""
        load_dotenv()
        self.engine = create_engine(os.getenv("DBURL"), echo=True)
        self.conn = self.engine.connect()
        print("Sucess")

    def closedb(self):
        self.conn.close()
