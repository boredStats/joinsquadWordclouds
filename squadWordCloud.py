# -*- coding: utf-8 -*-

import praw
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def joinText(textList):
    j = ''
    for t in textList:
        for w in t:
            j += w
    return j

def cleanText(words):
    return words.replace("game", "").replace("squad", "").replace("Squad", "").replace("server", "")

def squadWordcloud():
    apiKeys = []
    with open('./apiKeys.txt', 'r') as f:
        for k in f:
            apiKeys.append(str(k).rstrip('\n'))
    userAgent = 'joinsquadClientWordCloud'
    
    reddit = praw.Reddit(client_id=apiKeys[0], client_secret=apiKeys[1], user_agent=userAgent)
    
    numPosts = 300
    commentList = []
    titleList = []
    for submission in reddit.subreddit('joinsquad').new(limit=numPosts):
        titleList.append(submission.title)
#        for c in submission.comments:
#            commentList.append(c.body)
             
    words = joinText(titleList)
    cleaned = cleanText(words)
    fig, ax = plt.subplots()
    wcf = WordCloud(max_words=100, random_state=6, width=1600, height=900)
    wordcloud = wcf.generate(cleaned)
    ax.imshow(wordcloud, interpolation='lanczos')
    ax.axis("off")
    wordcloud.to_file("wordcloud.png")

if __name__ == "__main__":
    squadWordcloud()