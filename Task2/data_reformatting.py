# -*- coding: utf-8 -*-

# Load libraries
from typing import List, Dict
import pandas as pd
import json

# Create classes as per json schema
class Metric:
    '''class for metrics of the tweet'''
    
    def __init__(self, favorite_count, replies_count, retweet_count, unmetric_engagement_score):
        self.favorite_count = favorite_count
        self.replies_count = replies_count
        self.retweet_count = retweet_count
        self.unmetric_engagement = unmetric_engagement_score
        
    def to_dict(self):
        return {'favorite_count': self.favorite_count, 'replies_count': self.replies_count, 
                'retweet_count': self.retweet_count, 'unmetric_engagement' : self.unmetric_engagement}


class Tweet:
    '''class for tweet'''
    
    metrics: List[Metric]
    
    def __init__(self, tweet_id, tweet_type, tweet, url):
        self.tweet_id = tweet_id
        self.type = tweet_type
        self.tweet = tweet
        self.url = url
        
    def to_dict(self):    
        return {'tweet_id': self.tweet_id, 'type': self.type, 'tweet': self.tweet, 'url': self.url, 
                'metrics': [metric.to_dict() for metric in self.metrics]}
    
class Tweets_by_date:
    '''class to store list of '''
    
    tweets: List[Tweet]
    
    def __init__(self, tweet_created):
        self.tweet_created = tweet_created
        
    def to_dict(self):
        return {'tweet_created': self.tweet_created, 'tweets': [tweet.to_dict() for tweet in self.tweets]}
    

class Channel:
    '''Class for channel. e.g., Twitter'''
    
    tweets_by_date_list: List[Tweets_by_date]
    
    def __init__(self, name):
        self.name = name
        
    def to_dict(self):
        return {self.name: [tweet_by_date.to_dict() for tweet_by_date in self.tweets_by_date_list]}

    
class Company:
    '''Class for company. e.g., Huawei'''
    
    channel: Dict
    
    def __init__(self, name):
        self.name = name
        
    def to_dict(self):
        return {self.name: self.channel.to_dict()}
    


def reformat(df):
    '''
    Reads df and converts in dictionary
    input : pandas data frame
    return: dict
    '''    
    prev_row_tweet_date = ''
    prev_company = ''
    prev_channel = ''
    for i,row in df.iterrows():   
        # Initialize classes
        if prev_company!= row['company']:
            company = Company(row['company'])
        if prev_channel!= row['channel']:
            company.channel = Channel(row['channel'])
            company.channel.tweets_by_date_list = []
        if prev_row_tweet_date!= row["tweet_created"]:    
            tweets_by_date = Tweets_by_date( row["tweet_created"] )
            tweets_by_date.tweets = []
        
        # Populate values
        tweet = Tweet(row["tweet_id"], row["type"], row["tweet"], row["url"])
        tweet.metrics = []
        metric = Metric( row["favorite_count"] , row["replies_count"], row["retweet_count"], row["unmetric_engagement_score"])
        tweet.metrics.append(metric)
        
        # Add values to the classes
        tweets_by_date.tweets.append(tweet)
        if prev_row_tweet_date!= row["tweet_created"]:  
            company.channel.tweets_by_date_list.append(tweets_by_date)
        prev_row_tweet_date = row["tweet_created"]
        prev_channel = row['channel']
        prev_company = row['company']  
    return company.to_dict()
  
if __name__=="__main__":
    # Read data
    path = './Huawei.csv'
    df = pd.read_csv('./Huawei.csv')
    
    # Sort values
    df = df.sort_values(['company','channel','tweet_created','tweet_id'])
    # Reformat json
    result_dict = reformat(df)
   
    # Save json
    with open('result.json', 'w', encoding ='utf8') as json_file:
        json.dump(result_dict, json_file, ensure_ascii = True)