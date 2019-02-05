#!/usr/bin/env python3

import requests as r
import subprocess as sub
import json

group_id = 43492259
test_group_id = 47904833
bot_id = ""
test_bot_id = "c6c48e2c91f0f38efe62d44f2c"
token = ""
group_get_url = "http://api.groupme.com/v3/groups/"

from keys import *

group = r.get(group_get_url + str(group_id) + '?token=' + token).json()

users = {user['user_id']:user for user in group['response']['members']}
output = sub.run(['./get_todays.sh'], stdout=sub.PIPE).stdout.decode('utf-8')
#output = "40991635 16407411"
users = list(map(lambda a: users[a], output.split()))

body = dict()

text = "Hello $ and $! Don't pull a Ralph - get your lunches tomorrow"

attachment = dict()
attachment['type'] = "mentions"
loci = []
user_ids = []

for user in users:
    start = text.find('$')
    text = text.replace('$', '@' + user['nickname'], 1)
    length = 1 + len(user['nickname'])
    print(start, length)
    loci.append([start, length])
    user_ids.append(str(user['user_id']))

attachment['loci'] = loci
attachment['user_ids'] = user_ids

body['attachments'] = [attachment]
body['text'] = text
body['bot_id'] = test_bot_id

print(json.dumps(body))
r.post('https://api.groupme.com/v3/bots/post', json.dumps(body))
