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
r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning=True)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

subreddit = r.get_subreddit('wacomTest')

for submission in subreddit.get_new(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("Companion", submission.title, re.IGNORECASE):
            flat_comments = praw.helpers.flatten_tree(submission.comments)
            for comment in flat_comments:
                if comment.body == "do not delete":
                    if comment.author == submission.author:
                        submission.add_comment("This post has been approved")
                        print "Approved a Companion-related post"
                
                else:
                    submission.remove()
                    print "Deleted a Companion-related post"
            
        if re.search("Surface", submission.title, re.IGNORECASE):
            flat_comments = praw.helpers.flatten_tree(submission.comments)
            for comment in flat_comments:
                if comment.body == "do not delete":
                    if comment.author == submission.author:
                        submission.add_comment("This post has been approved")
                        print "Approved a Surface-related post"
                
                else:
                    submission.remove()
                    print "Deleted a Surface-related post"
        
        if re.search("Pro", submission.title, re.IGNORECASE):
            flat_comments = praw.helpers.flatten_tree(submission.comments)
            for comment in flat_comments:
                if comment.body == "do not delete":
                    if comment.author == submission.author:
                        submission.add_comment("This post has been approved")
                        print "Approved a Pro-related post"
                
                else:
                    submission.remove()
                    print "Deleted a Pro-related post"

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
            