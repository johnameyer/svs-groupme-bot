#!/usr/bin/env python3

import sys
import re
import datetime

monday = datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday())
friday = monday + datetime.timedelta(days=4)
today_rounded = datetime.date.today() + datetime.timedelta(days=(datetime.date.today().weekday() % 2))

file = "{:%-m %-d} - {:%-m %-d}.html".format(monday, friday)
day_name = "{:%A}".format(today_rounded)

mapping = {'csong1':'52560689','aduong1':'21343537','nmarcopo':'5576783','jmeyer5':'22102250','hlopez1':'20077360','rkarim':'33209469','rmoran1':'39322139','cfoley':'33524462','bblum1':'9812136','msalaman':'38190400','eyuan1':'22904273','sjohns37':'41041149','lwurl':'35947565','ywu6':'40991635','amascoli':'30590893','tsims2':'28952960','jrush2':'25117825','alamber2':'16407411','pbouchon':'45349456','drice4':'36759483','jruby1':'52655597','cchang7':'40845264','dadams12':'25929532'}
name_regex = '(' + '|'.join(mapping.keys()) + ')'

all_names = re.findall(name_regex, ''.join(open(file).readlines()))
selected = all_names[({'Monday':0, 'Wednesday':1,'Friday':2}[day_name]):6:3]

names = list(map(lambda a: mapping[a], selected))
print(" ".join(names))
