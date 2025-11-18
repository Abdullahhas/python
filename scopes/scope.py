username = "abdullah"

def func():
    username = 'hassan'  #local scope
    print(username)



print(username)  # global scope
func()


x = 99
def fun2(y):
    z = x + y
    return z


res = fun2(10)
print(res)


def f1():
    x = 88
    def f2():
        print(x)
    return f2

myRes = f1()
myRes()


def chaicoder (num) :
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)   # num values # ab f ke andr ik function aya (actual)
print(f(3))  # x value

