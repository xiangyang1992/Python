def printinfo(name, age):
    "打印任何字符"
    print("name:",name)
    print("age：",age)
    return

printinfo(age=50, name="keith")


# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("age:", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
# printinfo(name="runoob")