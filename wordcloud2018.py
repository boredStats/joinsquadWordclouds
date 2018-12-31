# -*- coding: utf-8 -*-

import random
import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

def joinText(textList):
    j = ''
    for t in textList:
        for w in t:
            j += w
    return j

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

with open("rawText.pkl","rb") as f:
    data = pkl.load(f)
    
titles = data['titles'] 
words = joinText(titles)

cl = ["game", "squad", "Squad"]
stopwords = set(STOPWORDS)
for c in cl:    
    stopwords.add(c)

fig, ax = plt.subplots()
wcf = WordCloud(random_state=6, width=1600, height=900, stopwords=stopwords)
wordcloud = wcf.generate(words)
ax.imshow(wordcloud, interpolation='lanczos')
ax.axis("off")
wordcloud.to_file("wordcloudRaw.png")

mask =  np.array(Image.open("mask.png"))
fig, ax = plt.subplots()
wcf = WordCloud(random_state=6, width=1600, height=900, stopwords=stopwords, mask=mask)
wordcloud = wcf.generate(words)
ax.imshow(wordcloud.recolor(3, grey_color_func), interpolation='lanczos')
ax.axis("off")
wordcloud.to_file("wordcloudMasked.png")