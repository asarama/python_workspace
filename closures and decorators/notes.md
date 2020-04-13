Python allows for local functions. Aka a function declared within another function.
Should mainly used for code organization and readability. Similar to lambdas but can contain more than one expression.

Python functions are just objects so they can be returned in function calls.

Python implements closures to ensure the garbage collector does not delete references for enclosed function call scopes. This useful in the function factory pattern. When functions have closures for their scope a dunder closure property is available for memory referencing.

```Python

# This is our function factory
def raise_to(exp):
    
    # This is the special function blueprint that we return
    def raise_to_exp(x):
        # exp is the object that is saved in our closure scope
        return x ** exp
    
    return raise_to_exp

cube = raise_to(3)
print(cube(2))
# 8

```

`nonlocal` and `global` keywords can be used to look outside your current function scope for reference hoisting.

```Python

import time
def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()

        # On first call return nothing
        # Mutate the last_called nonlocal variable
        if last_called is None:
            last_called = now
            return None
        
        # Return now time delta
        result = now - last_called
        last_called = now
        return result

    return elapsed

timer = make_timer()

timer()
# None

timer()
# 2.6923640223424

timer()
# 1.2012623947280

```

#### Decorators

Modify or enhance functions or methods without affecting their definitions.

```Python
@my_decorator
def my_function(x,y):
    return x + y
```

Not only functions can be used as decorators.
Classes can be used if they have the dunder call method.
Class instances can be used as well as long as they have the dunder call method.

In Python multiple decorators can be used. When evaluating decorators the decorator closest to the function definition runs first.

When using decorators we sometimes lose important function attributes (__name__, __doc__, etc).