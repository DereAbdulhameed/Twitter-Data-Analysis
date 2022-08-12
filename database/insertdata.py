from dataloader import DataLoader
from sqlalchemy import insert
from createtable import CreateTable
from connection import Connection
from sqlalchemy.orm import sessionmaker


class InsertData:
    """Insert data to the database"""
    def __init__(self, table):
        self.table = table
        DataLoader_obj= DataLoader('../data/','cleaned_tweet_data.csv')
        self.tweet_df = DataLoader_obj.read_csv()

    def insert_data(self):
        tweet = self.tweet_df
        stmt = ""
        for i in range(50):
            stmt = (
            insert(self.table).
            values(created_at=tweet.iloc[i, 0], 
            source=tweet.iloc[i, 1],
            original_text=tweet.iloc[i, 2],
            polarity = tweet.iloc[i, 3],
            subjectivity = tweet.iloc[i, 4],
            lang=tweet.iloc[i, 5],
            favorite_count=tweet.iloc[i, 6],
            retweet_count=tweet.iloc[i, 7],
            screen_count=tweet.iloc[i, 8],
            followers_count=tweet.iloc[i, 9],
            friends_count=tweet.iloc[i, 10],
            hashtags=tweet.iloc[i, 11],
            place=tweet.iloc[i, 12],
            clean_text=tweet.iloc[i, 13],
            )
            )

