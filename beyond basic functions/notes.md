Python is a functional programming language and thus functions can be passed as objects.

Functions in Python have two types of parameters; positional and keyword.

The dunder call method can be added to classes to make their instances callable like a function.

```Python
print("{:f}".format(_)) 
```

Will print the last line from the Python repl.

Conditional expressions are a drop in replacement for simple ternary operations.

```Python
value if expression else another_value
```

Lambda expressions are how anonymous functions are built in Python. Can only be a single expression.

```Python
add_lambda = lambda value_1, value_2: value_1 + value_2
add_lambda(1, 3)
# 4
```

Python can define functions which accept any number of input parameters.

```Python
# Positional
# lengths is a tuple
def hyper_volume(length, *lengths):
    volume = length
    for item in lengths:
        volume *= item
    return volume

# Keyword
# attributes is a dictionary
def tag(name, **attributes):
    html = '<' + name
    for key, value in attributes.items()
        html += ' {key}="{value}" '.format(key=key, value=str(value))
    
    html += '>'
    return html
```

tupls can be used to replace positional arguments, and dictionaries can be used to replace keyword arguments. The corresponding * and ** prefixes must be present in the call statement.