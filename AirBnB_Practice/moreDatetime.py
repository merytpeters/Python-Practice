#!/usr/bin/env python3

from datetime import datetime
from datetime import timedelta

date_now = datetime.now()
print(type(date_now))
print(date_now)
date_tomorrow = date_now + timedelta(days=1)
print(date_tomorrow)

a_dict = { 'my_date': date_now }
print(type(a_dict['my_date']))
print(a_dict)

# when datatime instance is a datastructure
print(date_now.strftime("%A"))
print(date_now.strftime("%A %d %B %Y at %H:%M:%S"))
