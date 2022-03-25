import sys


class Mynumber:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            c = self.a
            self.a += 1
            return c
        else:
            raise StopIteration

myclass = Mynumber()
myiter = iter(myclass)

for x in myiter:
    print(x)



if __name__ == '__main__':
    def fibonacci(n):
        a,b,counter = 0,1,0
        while True:
            if counter>n:
                return
            yield a
            a,b = b,a+b
            counter +=1

    f = fibonacci(10)

    while True:
        try:
            print(next(f),end=" ")
        except StopIteration:
            sys.exit()
