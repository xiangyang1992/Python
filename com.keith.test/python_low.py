# number = 7
# guess = -1
# print("猜数字游戏")
# while guess!=number:
#     guess = int(input("请输入你猜的数字："))
#     if guess == number:
#         print("你猜对了！")
#     elif guess > number:
#         print("你猜的太大了！")
#     elif guess<number:
#         print("你猜的太小了！")



for x in range(2,10):
    for n in range(2,x):
        if x % n == 0:
            print(x,'等于',n,'*',x//n)
            break
    else:
        print(x,' 是质数')
