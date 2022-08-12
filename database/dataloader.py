import pandas as pd
import os
class DataLoader:
    def __init__(self,dir_name,file_name):
        self.dir_name=dir_name
        self.file_name = file_name
    
 
    def read_csv(self):
        os.chdir(self.dir_name)
        tweets_df=pd.read_csv(self.file_name)
        return tweets_df
  