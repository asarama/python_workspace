# Example 1
# Apply a decorator which updates the return logic for all function below

def escape_unicode(function_reference):
    def wrap(*args, **kargs):
        function_return = function_reference(*args, **kargs)
        return ascii(function_return)
    
    return wrap

@escape_unicode
def vegetable():
    return 'carrot'

@escape_unicode
def animal()
    return 'cat'

@escape_unicode
def mineral():
    return 'limestone'


# Example 2
# Classes can be used as decorators as well. Here when we use the say_hello method the dunder call method of our CallCount class is executed.
# Using classes to decorate functions can add attributes to the function definition. Here we add the count attribute which keeps track of how many
# times it's function is called.

class CallCount:
    def __init__(self, function_reference)
        self.function_reference = function_reference
        self.count = 0

    def __call__(self, *args, **kargs):
        self.count += 1
        return self.function_reference(*args, **kargs)

@CallCount
def say_hello(name):
    print(f'Hello {name}')

# say_hello('a')
# Hello a
# say_hello('b')
# Hello b
# say_hello.count
# 2

# Example 3
# Class instances can also be used as decorators. They instead need the function reference in the dunder call method.
# This gives more flexibility to the decorator since we can set class parameters.
# To turn off tracing in this example all we need to do is set tracer.enabled = False

class Trace:
    def __init__(self, enabled = True):
        self.enabled = enabled

    def __call__(self, function_reference):

        def wrap(*args, **kargs):

            if self.enabled:
                print(f'Tracing {function_reference}')
                print(f'args {args}')
                print(f'kargs {kargs}')

            return function_reference(*args, **kargs)

        return wrap

tracer = Trace()

@tracer
def some_function(list):
    return zip(*list)