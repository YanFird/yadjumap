#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import argparse
from lxml import html


def getcookies(username,password):

    logon_url = "https://my.yad2.co.il/login.php"
    username = username
    password = password
    payload = {'USERNAME': '{USERNAME}'.format(USERNAME=username), 'PASSWORD': '{PASSWORD}'.format(PASSWORD=password)}
    r = requests.post(logon_url, data=payload)
    cookies = r.cookies

    return cookies


''''
def getParamsFromPage(cookies):

    url = "https://my.yad2.co.il/newOrder/index.php?action=personalAreaFeed&CatID=3&SubCatID=0"

    page = requests.get(url,cookies=cookies)
    print  page.content
    tree = html.fromstring(page.content)

    # This will create a list of buyers:

    cat_id = tree.xpath('//input[@name="CatID"]/@value')
    print cat_id
    cat_id = None
    order_id = None
    is_trade = None
    record_id = None
    state = None
    pass'''



''''not in use: only for test
    def getPersonalAreaPage(cookies,url):

    personalArea_url = url
    c = cookies
    r = requests.get(url, cookies=c)

    print r.text'''

def jumpit(cookies,cid,scid,oid):

    url = "https://my.yad2.co.il/newOrder/index.php?action=updateBounceListing&CatID={CID}&SubCatID={SCID}&OrderID={OID}".format(CID=cid,SCID=scid,OID=oid)
    h = {

        "Host": "my.yad2.co.il",
        "Connection": "keep-alive",
        "Origin": "https://my.yad2.co.il",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,he;q=0.8",
        "Pragma": "no - cache"
    }

    r = requests.post(url,headers=h,cookies=cookies)
    if "true" in r.text:
        print 'Its Works!! Great....'
    else: print "Oops... something didn't works, Maybe you tried to meany times, please try again later "
    #print r.text


def main():

    parser = argparse.ArgumentParser(prog='yadjump',description='Yad2 Autojump tool')

    parser.add_argument('-u', '--username', help='Yad2 username (your email)', required=True)
    parser.add_argument('-p', '--password',   help='Yad2 password', required=True)
    parser.add_argument('-cid', '--catid', help='Find CatID in "my ads" page', required=True)
    parser.add_argument('-scid', '--subcatid', help='Find SubCatID in "my ads" page', required=True)
    parser.add_argument('-oid', '--orderid', help='Find OrderID in "my ads" page', required=True)

    args = parser.parse_args()

    cookies = getcookies(args.username,args.password)

    jumpit(cookies,args.catid,args.subcatid,args.orderid)

if __name__ == "__main__":
    main()
