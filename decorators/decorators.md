STEP-BY-STEP DRY RUN
## 1) Python reads the def a_new_decorator(...) — decorator function is defined.

    No calls yet. Just a function object a_new_decorator exists.

    Memory:

    a_new_decorator → function object (decorator)

## 2) Python reads the def                 a_function_requiring_decoration(): ... plus the @a_new_decorator decorator.

    When Python sees @a_new_decorator above the function definition, it does this under the hood immediately after defining the function:
    def a_function_requiring_decoration():
    print("I am the function ...")

## AFTER definition, Python does:
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration) 

## So decorator function a_new_decorator is now called with the original function object as argument.

## Call:

a_new_decorator(a_func = original a_function_requiring_decoration function object)


### Inside a_new_decorator:

a_func (parameter) points to the original function object.

Then a_new_decorator creates the inner function wrapTheFunction (which closes over a_func) and returns the function object wrapTheFunction.

So after return:

#### a_function_requiring_decoration = wrapTheFunction

## 3) Now when you execute:

### a_function_requiring_decoration()

#### What actually happens?

Because a_function_requiring_decoration now refers to wrapTheFunction, this call does:

### wrapTheFunction()
