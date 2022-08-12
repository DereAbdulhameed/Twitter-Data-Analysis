import streamlit as st
from dataloader import DataLoader
import sys, os

sys.path.append(os.path.abspath(os.path.join("../..")))
class Display():
    def __init__(self):
        DataLoader_obj= DataLoader('../data/','cleaned_tweet_data.csv')
        tweet_df = DataLoader_obj.read_csv()
        st.dataframe(tweet_df)

dis = Display()
