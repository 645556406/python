import requests
import re
import urllib
import random
from time import sleep

#爬百度百科
def main():
    url="http://www.baidu.com"
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    print("%s",data)

if __name__ == '__main__':
    main()

