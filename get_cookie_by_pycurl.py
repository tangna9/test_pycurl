#-*- coding:utf-8 -*-

from io import BytesIO
import pycurl
import urllib
import time

username = 'tangna'
password = 'tangna'
shop_id = '18363'
login_url = 'http://adsmart.dangdang.com:8008/auth/login'
index_url = 'http://adsmart.dangdang.com:8008/index'

def login_get_cookie_by_pycurl():
    buf = BytesIO()
    curl = pycurl.Curl()
    curl.setopt(pycurl.COOKIEJAR, "D:\\cookies.txt")
    curl.setopt(pycurl.COOKIEFILE, "D:\\cookies.txt")
    curl.setopt(pycurl.URL, login_url)
    curl.setopt(curl.FOLLOWLOCATION, True)
    login_data = urllib.urlencode({'username': username,
                                    'password': password,
                                    'shopid': shop_id})
    curl.setopt(curl.POSTFIELDS, login_data)
    curl.setopt(curl.WRITEDATA, buf)

    curl.perform()
    curl.close()

    body = buf.getvalue()
    print body

if __name__ == "__main__":
    before_time = time.time()
    for i in xrange(0, 100):
        login_get_cookie_by_pycurl()
    after_time = time.time()
    print before_time, after_time, "time_diff:%s" %(after_time-before_time)