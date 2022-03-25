import sys

print("命令行参数如下：")
for i in sys.argv:
    print(i)

print('\n\nPython路径为：',sys.path,'\n')


print(dir(sys))


if __name__ == '__main__':
    table  = {'Google':1,'Runoob':2,'Taobao':3}
    for name,number in table.items():
        print('{0:10} ==> {1:10d}'.format(name,number))
        f = open("D:\MyPro\Python\main.py","w")
        f.write("Python")
        f.close()
