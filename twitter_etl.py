import tweepy
import json
import pandas as pd
from datetime import datetime
import s3fs

def run_twitter_etl():
    
    access_key = "GotTxL4Rl6GVyfG5jad1dl2xc"
    access_secret = "sc0t7w8HXFmoPUHTS45KrW8zeh43arqHuoUa45bJ3oi77cvelu"
    consumer_key = "1730118326087454721-vh2NXiLz1NWfVhAVOuwpAHra2NwFOD"
    consumer_Secret = "Wqomy586ukG4ANHdGrCd8zk8yZAGwHhNTGFhrzaZCccWb"

    #Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_Secret)

    #Creating an API object
    api = tweepy.API(auth)

    file_path = 'C:\DataEngi\airflowProjectTwtt\tweets.csv'
    df = pd.read_csv(file_path)







