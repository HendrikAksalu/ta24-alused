# API (Application Programming Interface) on kokkulepitud viis, kuidas tarkvararakendused omavahel suhtlevad, 
# võimaldades ühe rakenduse funktsioone või andmeid kasutada teise rakenduse poolt.
# pip on Pythonis kasutatav paketihaldur, mis võimaldab paigaldada, hallata ja eemaldada Pythoniga seotud teeke ja raamatukogusid.
# PRAW (Python Reddit API Wrapper) on Python'i teek, 
# mis lihtsustab Reddit'i API kasutamist, võimaldades lugeda ja postitada sisu Redditis.
#for submission in reddit.subreddit("learnpython").top(limit=10):
    #print(submission.title)

import praw
import re
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT'),
)
subreaddit_name = 'learnpython'
words = {}
commandWord = ['to', 'I', 'a', 'the', 'you', 'and', 'in', 'that', 'it', 'is', 'bits', 'of', 'with', 'bit', 'or', 'flag', 'not', 'need', 'for', 'do']
for submission in reddit.subreddit(subreaddit_name).hot(limit=20):
    submission.comments.replace_more(limit=0)
    for comment in submission.comments:
        for word in comment.body.split():
            word = (re.sub('^[^a-zaA-Z]*|[^a-zA-Z]*$', '',word))
            if word and word not in commandWord:
                if word in words:
                    words[word] +=1
                else:
                    words[word] = 1
sortedWords = sorted(words, key=words.get, reverse=True)
sortedWords = sortedWords[:20]
sizes = []
labels = []
print(sortedWords)
for w in sortedWords:
    sizes.append(words[w])
    labels.append(w)
plt.title('Enimlevinud sõnad: r/' + subreaddit_name)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.savefig('leanrpyhton.png')