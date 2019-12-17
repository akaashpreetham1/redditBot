# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:57:26 2019

@author: Akaash Preetham
"""

import praw
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("pythonforengineers")

for submission in subreddit.hot(limit = 5):
    if not os.path.isfile("Database.txt"):
        repliedposts = []
    else:
        with open("Database.txt", "r") as f:
            repliedposts = f.read()
            repliedposts = repliedposts.split('\n')
            repliedposts = list(filter(None, repliedposts))
        
    print("Title ", submission.title)
    print("Text ", submission.selftext)
    print("Score ", submission.score)
    print("\n")
    if submission.id not in repliedposts:
        if re.search("cow", submission.title, re.IGNORECASE):
            submission.reply("Booty bot says me 2")
            print("Bot replying to ", submission.title)
            repliedposts.append(submission.id)
            with open("Database.txt", "w") as f:
                for postID in repliedposts:
                    f.write(postID + '\n')
    
import pdb
import re
import os


