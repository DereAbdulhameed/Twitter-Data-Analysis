from connection import Connection
from sqlalchemy import MetaData,Table, Column, MetaData, Integer, String, Text, Float

class CreateTable:
    """A class for creating table"""
    def __init__(self, engine):
        self.metadata_obj = MetaData()
        self.clean_data = Table("CleanData", self.metadata_obj,
        Column('id', Integer,primary_key=True, autoincrement=True),
        Column('created_at', Text),
        Column('source', String(200)),
        Column('original_text', String(300)),
        Column('polarity', Float),
        Column('subjectivity', Float),
        Column('lang', Text),
        Column('favorite_count', Integer),
        Column('retweet_count', Integer),
        Column('original_author', Text),
        Column('screen_count', Integer),
        Column('followers_count', Integer),
        Column('friends_count', Integer),
        Column('hashtags', Text),
        Column('user_mentions', Text),
        Column('place', Text),
        Column('clean_text', Text))

        self.metadata_obj.create_all(engine)

