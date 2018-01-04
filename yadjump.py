#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import argparse



def getcookies(username,password):

    logon_url = "https://my.yad2.co.il/login.php"
    username = username
    password = password
    payload = {'USERNAME': '{USERNAME}'.format(USERNAME=username), 'PASSWORD': '{PASSWORD}'.format(PASSWORD=password)}
    r = requests.post(logon_url, data=payload)
    cookies = r.cookies

    return cookies


def getPersonalAreaPage(cookies,url):

    personalArea_url = url
    c = cookies
    r = requests.get(url, cookies=c)

    print r.text

def jumpit(cookies):


    url = "https://my.yad2.co.il/newOrder/index.php?action=updateBounceListing&CatID=3&SubCatID=0&OrderID=34616220"

    payload = {

        "action": "updateBounceListing",
        "CatID": 3,
        "SubCatID": 0,
        "OrderID": 34616220,
        "isTrader": 0,
        "RecordID": 14227558,
        "state": 2,
        "StatusID": 1,
        "Image1": "o3_0_1_35448_20180103110150.jpg",
        "Image2": "o3_0_2_35501_20180103110154.jpg",
    }


    h = {

        "Host": "my.yad2.co.il",
        "Connection": "keep-alive",
        "Origin": "https://my.yad2.co.il",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Referer": "https://my.yad2.co.il/newOrder/index.php?action=personalAreaViewDetails&CatID=3&SubCatID=0&OrderID=34616220",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,he;q=0.8",
        "Pragma": "no - cache"
    }

    #print cookies
    r = requests.post(url, data=json.dumps(payload),headers=h,cookies=cookies)
    print r.text



def main():

    parser = argparse.ArgumentParser(prog='yadjump',description='Yad2 Autojump tool')

    parser.add_argument('-u', '--username', help='Yad2 username', required=True)
    parser.add_argument('-p', '--password',   help='Yad2 password', required=True)

    args = parser.parse_args()

    #url = "http://my.yad2.co.il/newOrder/index.php?action=personalAreaIndex"
    #url = "https://my.yad2.co.il/newOrder/index.php?action=personalAreaFeed&CatID=3&SubCatID=0"
    cookies = getcookies(args.username,args.password)


    jumpit(cookies)


if __name__ == "__main__":
    main()
