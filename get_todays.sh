#!/bin/bash
mkdir tmp
cd tmp
curl -s "https://docs.google.com/spreadsheets/u/1/d/1EaJX8hGdjM3zvPyt-R7cdN5f6blh6SCq6tu9FndNHpk/export?format=zip&id=1EaJX8hGdjM3zvPyt-R7cdN5f6blh6SCq6tu9FndNHpk" > sheet.zip
unzip sheet.zip > /dev/null
../get_todays.py
cd ..
rm -rf tmp/
