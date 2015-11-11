'''
Created on Nov 11, 2015

Handles login using OAuth2

@author: Ryan
'''

app_id = 'TWjI69_JPEbrZQ'
app_secret = '5dqBlgic81ve0fioUw790XjgcWI'
app_uri = 'https://127.0.0.1:65010/authorize_callback'
app_ua = 'WacomMod 1.5'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = 'r3Tl0RmBqMpkYw_ayh6uWGNdYM4'
app_refresh = '45669536-JtPe7LMNpYkT7NJPktCifcIT1Eg'

import praw
def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r