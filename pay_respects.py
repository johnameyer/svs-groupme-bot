#!/usr/bin/env python3

import requests as r
import json
import sys
import random

from keys import *

body = dict()

body['text'] = 'F'
body['bot_id'] = bot_id

print(json.dumps(body))
r.post('https://api.groupme.com/v3/bots/post', json.dumps(body))
