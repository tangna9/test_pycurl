#-*- coding:utf-8 -*-
import pycurl
from StringIO import StringIO

#pycurl不提供对网络相应的存储，所以这里把返回结果写入内存，并读取
buf = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://www.baidu.com/')
c.setopt(c.WRITEDATA, buf)
c.perform()
c.close()

body = buf.getvalue()
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
print(body)