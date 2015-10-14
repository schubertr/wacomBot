'''
Created on Oct 14, 2015

@author: schubertr
'''

import praw
import pdb
import re
import os
from config_bot import *

user_agent = ("wacomMod 0.1")
r = praw.Reddit(user_agent=user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASS,disable_warning=True)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

subreddit = r.get_subreddit('stirusTEST')

for submission in subreddit.get_hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("Companion", submission.title, re.IGNORECASE):
            if "do not delete" in submission.comments:
                submission.add_comment("This post has been approved")
            else:
                submission.remove()
            
        if re.search("Surface", submission.title, re.IGNORECASE):
            if "do not delete" in submission.comments:
                submission.add_comment("This post has been approved")
            else:
                submission.remove()
        
        if re.search("Pro", submission.title, re.IGNORECASE):
            if "do not delete" in submission.comments:
                submission.add_comment("This post has been approved")
            else:
                submission.remove()

print "Bot replying to : ", submission.title
posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
            