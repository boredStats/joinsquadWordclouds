# -*- coding: utf-8 -*-

import time
import praw
import pickle as pkl
import datetime as dt
from psaw import PushshiftAPI

def getData(keypath):
    start = time.time()
    k = []
    with open(keypath, "r") as f:
        for s in f:
            k.append(str(s).rstrip('\n'))
            
    agent = 'joinsquadClient'
    r = praw.Reddit(client_id=k[0], client_secret=k[1], user_agent=agent)
    api = PushshiftAPI(r)
    
    kwargs = {'after':int(dt.datetime(2018, 1, 1).timestamp()),
              'subreddit':'joinsquad',
              'filter':['url', 'author', 'title', 'subreddit'],
              'limit':99999}
    a = list(api.search_submissions(**kwargs))
    
    with open("submissionData.pkl", "wb") as f:
        pkl.dump(a, f)
    print("Download runtime : %.02f seconds" % (time.time() - start))   
    return a
    
if __name__ == "__main__":
    path = r"./keys/apiKeys_.txt"
    submissions = getData(path)