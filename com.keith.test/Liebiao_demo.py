# names = ['bobo','tom','alice','jerry','wendy','smith']
# name_news = [name.upper() for name in names if len(name)>3]
# print(name_news)
#
#
# # 计算30以内能被3整除的整数
# multiples = [num for num in range(30) if num%3==0]
# print(multiples)
#
#
# listdemo = ['Google','Runoob', 'Taobao']
# newdic = {key:len(key) for key in listdemo}
# print(newdic)
#
# dict = {x:x**2 for x in range(10)}
# print(dict)


a,b = 0,1
while b<10:
    print(b)
    a,b = b,a+b