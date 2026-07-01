# Default Argument values

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# This function can be called in several ways:

# giving only the mandatory argument: ask_ok('Do you really want to quit?')

# giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)

# or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


i = 5

def f(arg=i):
    print(arg)

i = 6
f()


#  har function call me wahi same list reuse hoti rahi.
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# [1] , [1,2] , [1,2,3]

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:z
def f(a, L=None):   # ab kkoi list ni di gayi
    if L is None:
        L = []
    L.append(a)
    return L


#  output [1] [2] [3]