__author__ = 'sirwang'

product_list = [
    ('Iphone','5800'),
    ('Mac Pro','12000'),
    ('Bike','800'),
    ('Watch','10600'),
    ('Coffee','12600'),
    ('Python','600'),
]

user_list = [
    ('Iphone','5800'),
    ('Mac Pro','12000'),
    ('Bike','800'),
    ('Watch','10600'),
    ('Coffee','12600'),
    ('Python','600'),
]

client_input = input("请输入工资：")
if client_input.isdigit():
    client_input = int(client_input)
    while True:

        for index,item in enumerate(product_list):
            print(index,item)
        user_chooice = input("\r\n选择要买的商品编号:")
        if user_chooice.isdigit():
            user_chooice = int(user_chooice)
            if user_chooice >= 0 and  user_chooice <= len(user_list):
                for index, item in enumerate(user_list):
                    print(index,item)
                shop_xuanze = user_list[user_chooice][1]
                gongzi_shengyu = int(client_input) - int(shop_xuanze)
            else:
                exit()
        else:
            print("输入的不是数字")
            exit()
        print("\r\n你的工资还剩余%s" % gongzi_shengyu)

        break

else:
    print("输入的不是数字")
    exit()

