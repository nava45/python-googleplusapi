#!/usr/bin/env python
# coding: utf-8

from pprint import pprint

# my api
import gplusapi

user_id = '101170646732501865584'
plus = gplusapi.GooglePlusAPI()


ret = plus.get_user(user_id)
pprint(ret)

#ret = plus.get_posts(user_id)
#pprint(ret)

#ret = plus.get_followers(user_id)
#pprint(ret)

#ret = plus.get_followings(user_id)
#pprint(ret)
