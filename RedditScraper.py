#!/usr/bin/env python
# coding: utf-8

# In[49]:


import praw
import pandas as pd
import datetime as dt
import openpyxl



# In[52]:


reddit = praw.Reddit(client_id='fsx7ntWwH24AZA',                      client_secret='VLsE4zgvAdtpfeKgcksKIa1bKC4',                      user_agent='Reddit Scraper',                      username='NMBLsummer2020',                      password='stanford')

subredditName = input("Enter Subreddit Name: r/")
subreddit = reddit.subreddit(subredditName)

topics_dict = { "title":[], "author":[],                 "score":[],                 "id":[], "url":[],                 "comms_num": [],                 "created": [],                 "body":[], "comments":[]}

searchAnswer = input("Would you like to search for a specific keyword? (Y/N): ")
if(searchAnswer == "Y"):
    searchWord = input("Enter key search words separated by + signs or ENTER if finished: ")
    history = set()
    while(searchWord != ""):
        top_subreddit = subreddit.search(searchWord, limit = None)
        for submission in top_subreddit:
            if(submission not in history):
                print(submission.title)
                topics_dict["title"].append(submission.title)
                topics_dict["author"].append(submission.author)
                topics_dict["score"].append(submission.score)
                topics_dict["id"].append(submission.id)
                topics_dict["url"].append(submission.url)
                topics_dict["comms_num"].append(submission.num_comments)
                topics_dict["created"].append(submission.created)
                topics_dict["body"].append(submission.selftext)
                submission.comments.replace_more(limit=None)
                comments = submission.comments.list()

                topics_dict["comments"].append("")
                if (comments.__len__() > 0):
                    for index in range(0, comments.__len__()):
                        topics_dict["comments"].append(comments[index].body)
                        topics_dict["author"].append(comments[index].author)
                        topics_dict["title"].append("")
                        topics_dict["score"].append("")
                        topics_dict["id"].append("")
                        topics_dict["url"].append("")
                        topics_dict["comms_num"].append("")
                        topics_dict["created"].append(comments[index].created)
                        topics_dict["body"].append("")
            history.add(submission)
        searchWord = input("Enter key search words separated by + signs or ENTER if finished: ")
else:
    top_subreddit = subreddit.top("all")
    for submission in top_subreddit:
        print(submission.title)
        topics_dict["title"].append(submission.title)
        topics_dict["author"].append(submission.author)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)
        submission.comments.replace_more(limit=None)
        comments = submission.comments.list()

        topics_dict["comments"].append("")
        if (comments.__len__() > 0):
            for index in range(0, comments.__len__()):
                topics_dict["comments"].append(comments[index].body)
                topics_dict["author"].append(comments[index].author)
                topics_dict["title"].append("")
                topics_dict["score"].append("")
                topics_dict["id"].append("")
                topics_dict["url"].append("")
                topics_dict["comms_num"].append("")
                topics_dict["created"].append(comments[index].created)
                topics_dict["body"].append("")



# In[53]:




# In[54]:


topics_data = pd.DataFrame(topics_dict)


# In[55]:


topics_data


# In[56]:


def get_date(created):
    return dt.datetime.fromtimestamp(created)
_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)
topics_data


# In[57]:

fileName = input("Enter Output File Name: ") + ".csv"
topics_data.to_csv(fileName, index=False)
#topics_data.to_excel("Testing1.xlsx", index=False)


# In[ ]:




