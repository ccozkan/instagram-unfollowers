#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from insta import Instagram
import os
import json
import pystache
import io
import webbrowser


numer = sys.argv[1]

#modify here
insta = Instagram('foousername', 'foopassword')                                   


if insta.login() == False:
    print "Login failed"
    sys.exit(2)

temp = insta.getTotalUserFeed(numer)
followers = insta.getTotalFollowers(numer)
followings = insta.getTotalFollowings(numer)
followersnum=len(followers)
followingsnum=len(followings)



notfollowedback = []
for fr in followings:
    flag = True
    for fg in followers:
        if fg["pk"] == fr["pk"]:
            flag = False
            break
    if flag:
        notfollowedback.append(fr)


newnotfollowedback = []
if os.path.exists('notfollowedback.json'):
    with open('notfollowedback.json') as data_file:
        oldnotfollowedback = json.load(data_file)
        for fr in notfollowedback:
            flag = True
            for fg in oldnotfollowedback:
                if fg["pk"] == fr["pk"]:
                    flag = False
                    break
            if flag:
                newnotfollowedback.append(fr)
                mesaje='echo "'+str(fr)+' ---new not followed back--- " | sendxmpp -t foo@fooxmpp.com'
                os.system(mesaje)

newfollowers = []
if os.path.exists('followers.json'):
    with open('followers.json') as data_file:
        oldfollowers = json.load(data_file)
        for fr in followers:
            flag = True
            for fg in oldfollowers:
                if fg["pk"] == fr["pk"]:
                    flag = False
                    break
            if flag:
                newfollowers.append(fr)

newunfollowers = []
if os.path.exists('followers.json'):
    with open('followers.json') as data_file:
        oldfollowers = json.load(data_file)
        for fr in oldfollowers:
            flag = True
            for fg in followers:
                if fg["pk"] == fr["pk"]:
                    flag = False
                    break
            if flag:
                newunfollowers.append(fr)

newfollowings = []
if os.path.exists('followings.json'):
    with open('followings.json') as data_file:
        oldfollowings = json.load(data_file)
        for fr in followings:
            flag = True
            for fg in oldfollowings:
                if fg["pk"] == fr["pk"]:
                    flag = False
                    break
            if flag:
                newfollowings.append(fr)


with open('followers.json', 'w') as outfile:
    json.dump(followers, outfile)

with open('followings.json', 'w') as outfile:
    json.dump(followings, outfile)


with open('notfollowedback.json', 'w') as outfile:
    json.dump(notfollowedback, outfile)

file = open('template-lite.tpl', 'r')
html = file.readlines()
tpl = ''
for line in html:
    tpl = tpl + " " + line



data = {
    "username": [followersnum, followingsnum],
    "notback": notfollowedback,
    "newfollowers": newfollowers,
    "newunfollowers":newunfollowers,
    "newfollowings": newfollowings,
}

output = pystache.render(tpl, data)
with io.open('output-lite.html', 'w', encoding='utf8') as f:
    f.write(output)
    
