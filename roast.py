#!/usr/bin/env python3

import requests as r
import json
import sys
import random

from keys import *



body = dict()

text = ''

roasts = {
	'eddie':'I would roast all the teams Eddie is a "fan" of but I dont have that much memory',
	'horacio':'Hey Horacio try not to order food at 1 AM and then fall asleep before it arrives again',
	'catbot':'ItS oFf Rn'
}

body['text'] = roasts[sys.argv[1].lower()] if (len(sys.argv) > 1) else random.choice(roasts.values())
body['bot_id'] = bot_id
if sys.argv[1].lower() == 'catbot':
	body['picture_url'] = 'https://i.groupme.com/680x440.png.03a2453e22984929ad0afb521b78ceb9'

print(json.dumps(body))
r.post('https://api.groupme.com/v3/bots/post', json.dumps(body))
