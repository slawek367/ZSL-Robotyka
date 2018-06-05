#tutorial
#https://chyla.org/blog/Python_-_Dekoratory/
#args and kwargs: https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3

'''
#EXAMPLE:

from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('Calling decorated function')
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')
'''

''' decorator examples which change all parameters to abs '''
from functools import wraps

def abs_decorator_basic(f):
    def wrapper(a, b, c):
        a = abs(a)
        b = abs(b)
        c = abs(c)
        return f(a, b, c)
    return wrapper

def abs_decorator(f):
    @wraps(f)
    def wrapper(a, b, c):
        a = abs(a)
        b = abs(b)
        c = abs(c)
        return f(a, b, c)
    return wrapper

def dodaj(a, b, c):
    return a + b + c

@abs_decorator_basic
def dodaj2(a, b, c):
    return a + b + c

@abs_decorator
def dodaj3(a, b, c):
    return a + b + c

print(dodaj(2, 3, -4))
print(dodaj2(2, 3, -4))
print(dodaj3(2, 3, -4))
print(dodaj2.__name__)
print(dodaj3.__name__)
