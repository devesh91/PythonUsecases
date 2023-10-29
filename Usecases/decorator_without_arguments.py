


def decorate_my_func(func):


    def inner(*args,**kwargs):
        #Accessing function arguments
        print(*args,**kwargs)
        return func(*args, **kwargs)


    return inner


@decorate_my_func
def my_func(a,b):
    print("my func got called")
    return None

my_func(1,2)