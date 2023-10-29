
def my_decorator(arg):
    print("argument of decorator",arg)
    def inner_decorator(func):
        def wrapped(*args, **kwargs):
            print('arguments of original function',*args,kwargs)
            response = func(*args, **kwargs)
            print('after function')
            return response
        print('decorating', func, 'with argument', arg)
        return wrapped
    return inner_decorator

@my_decorator('foo')
def my_function(a, b,x=None):
    print('in function')
    return a + b


my_function(1,2,x=1)
