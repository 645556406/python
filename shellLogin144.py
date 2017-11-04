import requests
import re
import urllib
import random
from time import sleep

#爬百度百科
def main():
    url="http://www.cnblogs.com/freeweb/p/5425554.html"
    data = urllib.request.urlopen(url).readlines()
    #data = data.decode('UTF-8')
    opBaiduCunChu=open('1.txt','a+')
    opBaiduCunChu.write(str(data))
    opBaiduCunChu.close()
    print('%s'%data)

if __name__ == '__main__':
    main()

