# Returning functions from within functions:

#It is not necessary to execute a function within another function, we can return it as an output as well:

def hi(name = "yasoob"):

    def greet():
        return "now you are in the greet() function"
    
    def welcome():
        return "now you are in the welcome() function"
    
    if name == 'yasoob':
        return greet
    else:
        return welcome
    
a = hi()
print(a)

#outputs: <function hi.<locals>.greet at 0x000002C8D8BA8FE0>

#This clearly shows that `a` now points to the greet() function in hi()
#Now try this

print(a()) # or hi()()
#outputs: now you are in the greet() function

