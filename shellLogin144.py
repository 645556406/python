from urllib import request
import os

#爬百度
def main():
    url="http://www.baidu.com/"
    data = request.urlopen(url).read()
    #data = data.decode('UTF-8')
    data=str(data)
    print(type(data))
    print("%s",data)
    wBaiDu=open('1.txt','a+')
    wBaiDu.write(data+'\n')
    wBaiDu.close()

if __name__ == '__main__':
    main()



