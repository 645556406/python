__author__ = 'sirwang'

######### 文件读取
# 十分占内存
with open("1.txt",'r',encoding="utf-8") as f:
    for index,line in enumerate(f.readlines()):
        if index == 2:
            print("-----我是第三行--------")
            continue
        else:
            print(line.strip())
        if index == 3:
            print('\r\n')
        else:
            pass

# 优秀的写法
with open("1.txt",'r',encoding="utf-8") as f:
    count = 0
    for line in f:
        count += 1
        if count == 3:
            print("-----我是第三行--------")
            continue
        else:
            print(line.strip())

# tell()打印文件句柄指针的位置
# seek()移动指针到指定位置 seek(0) 移动到开头
# readable()判断文件是否可读
# flush()方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
# truncate(20)从读取的文件开头截取20个字符
f = open("1.txt",'r',encoding="utf-8")
print(f.tell())
data = f.readline()
print(data)
print(f.tell())
f.seek(10)
print(f.readline())
print(f.encoding)
print(f.buffer)
print(f.fileno())

"""
import sys,time
for i in range(20):
    sys.stdout.write("#")
    time.sleep(0.5)
"""

