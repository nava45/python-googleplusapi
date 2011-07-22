#!/usr/bin/env python
# coding: utf-8

import time
import urllib
import urllib2
import json 
import re
import decimal

from pprint import pprint

class GooglePlusAPI:

    PROFILES_URL = 'https://plus.google.com/_/profiles/get/USER_ID'
    FOLLOWING_URL = 'https://plus.google.com/_/socialgraph/lookup/visible/?o=[null,null,"USER_ID"]'
    FOLLOWER_URL = 'https://plus.google.com/_/socialgraph/lookup/incoming/?o=[null,null,"USER_ID"]&n=1000'
    POST_URL = 'https://plus.google.com/_/stream/getactivities/USER_ID/?sp=[1,2,"USER_ID",null,null,null,null,"social.google.com",[]]&rt=j'

    def __init__(self):
        self._uid = False
        self._nickname = False

    def login(self, username, password):
        pass

    def get_json(self, url):
        try:
            response = urllib2.urlopen(url)
            ret = response.read()
            raw = ret[5:]
            raw = raw.replace('\n', '')
            raw = re.sub(r'([[{,]),', r'\1null,', raw)
            raw = re.sub(r',([]},])', r',null\1', raw)
            if 'getactivities' in url:
                raw = ','.join(raw.split(',')[:-1]) + ']'
                #pprint(raw)

            #pprint(raw)
            ret = json.loads(raw)
            #pprint(ret)
        except:
            raise

        return ret

    def add_post(self, content, to_circles=[]):
        pass

    def get_posts(self, id):
        url = self.POST_URL.replace('USER_ID', id)
        posts = []

        try:
            ret = self.get_json(url)
            raws = ret[0][0][1][0]
            for raw in raws:
                post = {}
                post['id'] = raw[21].split('/')[0]
                post['author'] = raw[3]
                post['subject'] = raw[4]
                post['source'] = raw[2]
                post['timestamp'] = raw[30]

                posts.append(post)
        except:
            raise

        return posts

    def get_post(self):
        pass

    def get_responses(self):
        pass

    def get_response(self):
        pass

    def response_to(self):
        pass

    def get_followers(self, id):
        url = self.FOLLOWER_URL.replace('USER_ID', id)
        followers = []

        try:
            ret = self.get_json(url)
            raws = [{'user_id': item[0][2], 'user_data': item[2]} for item in ret[2]]
            for raw in raws:
                follower = {}
                follower['id'] = raw['user_id']
                follower['nickname'] = raw['user_data'][0]

                followers.append(follower)

            #pprint(followers)
        except:
            raise

        return followers

    def get_followings(self, id):
        url = self.FOLLOWING_URL.replace('USER_ID', id)
        followings = []

        try:
            ret = self.get_json(url)
            raws = [{'user_id': item[0][2], 'user_data': item[2]} for item in ret[2]]
            for raw in raws:
                following = {}
                following['id'] = raw['user_id']
                following['nickname'] = raw['user_data'][0]

                followings.append(following)

            #pprint(followings)
        except:
            raise

        return followings

    def get_alerts(self):
        pass

    def be_friends(self):
        pass

    def remove_friends(self):
        pass

    def get_user(self, id):
        url = self.PROFILES_URL.replace('USER_ID', id)

        try:
            ret = self.get_json(url)
            #pprint(ret[1][2])
            user = {}
            user['id'] = ret[1][0]
            user['first_name'] = ret[1][2][4][1]
            user['last_name'] = ret[1][2][4][2]
            user['full_name'] = ret[1][2][4][3]
            user['alternative_names'] = ret[1][2][5][1]
            user['avatar_url'] = 'https:' + ret[1][2][3]
            user['profile_url'] = ret[1][2][2]
        except:
            raise

        return user

    def get_username(self, id):
        pass

