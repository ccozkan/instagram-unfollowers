#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from insta import Instagram
import os
import json
import pystache
import io
import webbrowser
import random

numer = sys.argv[1]
print " ~ Connecting to Instagram"
#modify here
insta = Instagram('usernamefoo', 'passfordfoo')                                   


if insta.login() == False:
    print "Login failed"
    sys.exit(2)
print " ~ Sending request to Instagram , fetching your feeds"
temp = insta.getTotalUserFeed(numer)
likedUsers = {}
for item in temp:
    insta.getMediaLikers(item["id"])
    test = insta.LastJson["users"]
    for user in test:
        if user["username"] not in likedUsers:
            data = {}
            data["count"] = 1
            data["name"] = user["full_name"]
            data["image"] = user["profile_pic_url"]
            data["username"] = user["username"]
            likedUsers[user["username"]] = data
        else:
            likedUsers[user["username"]]["count"] += 1

print " ~ Sending request to Instagram , fetching followers"
followers = insta.getTotalFollowers(numer)
print " ~ Sending request to Instagram , fetching followings"
followings = insta.getTotalFollowings(numer)
followersnum=len(followers)
followingsnum=len(followings)
print " ~ Processing..."
fans = []
for fr in followers:
    flag = True
    for fg in followings:
        if fg["pk"] == fr["pk"]:
            flag = False
            break
    if flag:
        fans.append(fr)

notfollowedback = []
for fr in followings:
    flag = True
    for fg in followers:
        if fg["pk"] == fr["pk"]:
            flag = False
            break
    if flag:
        notfollowedback.append(fr)

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

neverLiked = []
for follower in followers:
    if follower["username"] not in likedUsers:
        neverLiked.append(follower)

file = open('template.tpl', 'r')
html = file.readlines()
tpl = ''
for line in html:
    tpl = tpl + " " + line

likedUsers = sorted(likedUsers.values(),
                    key=lambda x: x["count"], reverse=True)


data = {
    "username": [followersnum, followingsnum],
    "notback": notfollowedback,
    "newfollowers": newfollowers,
    "newunfollowers":newunfollowers,
    "newfollowings": newfollowings,
    "bestlikers": likedUsers[:20],
#    "badlikers": likedUsers[len(likedUsers) - 10:],
    #"neverliked": neverLiked[0:10]
    "neverliked": random.sample(neverLiked,10)
}

print " ~ Creating output.html"
output = pystache.render(tpl, data)
with io.open('output.html', 'w', encoding='utf8') as f:
    f.write(output)
    
#webbrowser.open_new_tab('output.html')
