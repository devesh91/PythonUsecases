"""This file contains example of decorator with arguments"""

def make_pretty(*args, **kwargs):

    def inner(func):

        print("my func just got decorated")
        print("api name {}".format(kwargs['x']))
        #argumennts can be accessed from args & kwargs
        print(*args)
        print(kwargs)


        return func

    return inner


@make_pretty((1,2,3),x="my_func_api")
def my_func(a,b):
    return "Hello World"


print(my_func(1,2))