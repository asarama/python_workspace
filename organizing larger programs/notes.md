Python organizes code into modules. Usually a single file.

A package is a module which can contain multiple modules. Usually a directory. Adding a __init__.py to the directory will make it a package. This init file actually executes when importing the package. This is a great place to hoist classes by importing them.

``` python
from some_package.some_module import SomeClass
```

Now user can use our class SomeClass by just importing our package.

All modules can be imported via the import command.

Python looks for modules recursively through all directories available in sys.path.

You can manually add paths to sys.path or update the PYTHONPATH environment variable.

