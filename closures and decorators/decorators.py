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