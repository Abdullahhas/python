# Defining functions within functions:

def hi(name = "yasoob"):
    print("now you are in hi() function")

    def greet():
        return "now you are in greet() function"
    
    def welcome():
        return "now you are in the welcome() function"


    print(greet())
    print(welcome())
    print("now you are back in hi() function")


hi()


# This shows that whenever you call hi(), greet() and welcome()
# are also called. However the greet() and welcome() functions
# are not available outside the hi() function e.g:

greet()
#outputs: NameError: name 'greet' is not defined