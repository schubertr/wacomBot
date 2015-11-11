'''
Created on Oct 14, 2015

@author: Ryan
'''

import praw
import re
import os
import obot

def countComments(flat_comments): #function to count number of comments on a post
    count = 0
    for comment in flat_comments:
        count += 1
    return count

r = obot.login() #logins to /u/wacomBot using OAuth2

safe_word = "do not delete" #put the phrase OP can comment to have the bot not delete the post here

if not os.path.isfile("posts_replied_to.txt"): #creates or opens the file used to store posts replied to
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

subreddit = r.get_subreddit('wacomTest') #put the subreddit name here

for submission in subreddit.get_new(limit=10): #gets the 10 newest submissions in the subreddit
    if submission.id not in posts_replied_to: #if the current post is not one we checked already
        if re.search("Companion", submission.title, re.IGNORECASE): #locates post with keyword
            print("found companion post")
            rem = 0
            flat_comments = praw.helpers.flatten_tree(submission.comments) #gets comments
            num = countComments(flat_comments) #counts comments
            
            if num == 0: #if no comments, remove post
                submission.remove()
                print "Deleted a Companion-related post"
                posts_replied_to.append(submission.id)
                
            else:
                for comment in flat_comments:
                    if comment.body == safe_word: #if OP commented the phrase, approve the post
                        if comment.author == submission.author:
                            submission.add_comment("This post has been approved")
                            print "Approved a Companion-related post"
                            posts_replied_to.append(submission.id)  
                            rem = 1
                
                if rem != 1: #if not, delete it
                    submission.remove()
                    print "Deleted a Companion-related post"
                    posts_replied_to.append(submission.id)  
            
        if re.search("Surface", submission.title, re.IGNORECASE): #follows same code as above, but with "Surface"
            print("found surface post")
            rem = 0
            flat_comments = praw.helpers.flatten_tree(submission.comments)
            num = countComments(flat_comments)
            
            if num == 0:
                submission.remove()
                print "Deleted a surface-related post"
                posts_replied_to.append(submission.id)
                
            else:
                for comment in flat_comments:
                    if comment.body == safe_word:
                        if comment.author == submission.author:
                            submission.add_comment("This post has been approved")
                            print "Approved a Surface-related post"
                            posts_replied_to.append(submission.id)
                            rem = 1
                
                if rem != 1:
                    submission.remove()
                    print "Deleted a Surface-related post"
                    posts_replied_to.append(submission.id)
        
        if re.search("Pro", submission.title, re.IGNORECASE): #follows same code as above, but with "Pro"
            print("found a pro post")
            rem = 0
            flat_comments = praw.helpers.flatten_tree(submission.comments)
            num = countComments(flat_comments)
            
            if num == 0:
                submission.remove()
                print "Deleted a Pro-related post"
                posts_replied_to.append(submission.id)
                
            else:
                for comment in flat_comments:
                    if comment.body == safe_word:
                        if comment.author == submission.author:
                            submission.add_comment("This post has been approved")
                            print "Approved a Pro-related post"
                            posts_replied_to.append(submission.id)
                            rem = 1
                
                if rem != 1:
                    submission.remove()
                    print "Deleted a Pro-related post"
                    posts_replied_to.append(submission.id)             

with open("posts_replied_to.txt", "w") as f: #saves the posts we checked in the file so we don't check them again next time
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
            