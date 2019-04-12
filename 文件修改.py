import sys

#参数1
find_str = sys.argv[1]
#参数2
replace_str = sys.argv[2]
with open("1.txt",'r+',encoding='utf-8') as f:
# 如果要打开多个文件
# with open("1.txt",'r+',encoding='utf-8') as f: \
#     open("2.txt",'r+',encoding='utf-8') as f2:
    for line in f:
        if "libs" in line:
            line = line.replace("libs","+++++++++++++++")
        f.write(line)
    f.seek(0)
    print(f.readline().strip())