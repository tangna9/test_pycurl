#-*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
import time

username = 'tangna'
password = 'tangna'
shop_id = '18363'
login_url = 'http://adsmart.dangdang.com:8008/auth/login'
index_url = 'http://adsmart.dangdang.com:8008/index'

def get_cookie_info():

    #捕获cookie
    cj = cookielib.CookieJar()

    login_data = urllib.urlencode({'username': username,
                                   'password': password,
                                   'shopid': shop_id})
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.open(login_url, login_data)
    for cookie in cj:
        print "---First time cookie:%s --> %s" %(cookie.name, cookie.value)

    resp = opener.open(index_url)
    print resp.read()
    # for cookie in cj:
    #     print "---Second time cookie:%s --> %s" %(cookie.name, cookie.value)

if __name__ == '__main__':
    #get_cookie_info()

    before_time = time.time()
    for i in xrange(0, 100):
        get_cookie_info()
    after_time = time.time()
    print before_time, after_time, "time_diff:%s" %(after_time-before_time)