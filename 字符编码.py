#-*- coding:utf-8 -*-
import sys

code_default = sys.getdefaultencoding()
print("python3默认编码是："+code_default+",但是字符串默认是unicode")

s = "你好世界"
# utf-8转gbk，要先剑utf-8转换成unicode，再把Unicode转换成gbk，反之亦然
# 因为s默认是unicode，所以要先encode，然后再进行对应的转换
d = s.encode("utf-8")
print(d)

# python3中转换后，要再decode一下才能看见字符串
f = d.decode("utf-8").encode("gbk").decode("gbk")
print(f)


# gbk转utf-8
# c = d.encode("gbk").decode("utf-8")
# print(c)
