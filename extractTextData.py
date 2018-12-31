# -*- coding: utf-8 -*-

import praw
import pickle as pkl

with open("submissionData.pkl","rb") as f:
    submissions = pkl.load(f)
commentList, titleList = [], []

for i, submission in enumerate(submissions):
    titleList.append(submission.title)
    for c in submission.comments:
        if isinstance(c, praw.models.reddit.comment.Comment):
            commentList.append(c.body)

data = {'comments':commentList,
        'titles':titleList}

with open("rawText.pkl", "wb") as g:
    pkl.dump(data, g)