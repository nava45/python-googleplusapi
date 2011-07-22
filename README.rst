Unofficial Python Google Plus API
==================================

This is a buggy and lazy version of google plus API.

Current Version could only provide:

    1. GooglePlusAPI.get_user(<user_id>)

    2. GooglePlusAPI.get_posts(<user_id>)

    3. GooglePlusAPI.get_followers(<user_id>)

    4. GooglePlusAPI.get_followings(<user_id>)

Usage
------
::

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

Todos
------

1. full clone php version of google plus api

2. other methods::

    def login()
    def add_post()
    def get_post()
    def get_responses()
    def get_response()
    def response_to()
    def get_followers()
    def get_followings()
    def get_alerts()
    def be_friends()
    def remove_friends()

and others...

References
----------
https://github.com/jmstriegel/php.googleplusapi

http://code.google.com/p/javaplus/

