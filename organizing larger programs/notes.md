Python organizes code into modules. Usually a single file.

A package is a module which can contain multiple modules. Usually a directory. Adding a __init__.py to the directory will make it a package. This init file actually executes when importing the package. This is a great place to hoist classes by importing them.

``` python
from some_package.some_module import SomeClass
```

Now user can use our class SomeClass by just importing our package.

All modules can be imported via the import command.

Python looks for modules recursively through all directories available in sys.path.

You can manually add paths to sys.path or update the PYTHONPATH environment variable.

__all__ attribute can be used to control what is imported when using the import statement

``` python
from some_package import *
```

Namespace packages are used to house complex packages that require modules from multiple directories. These have no __init__.py files add thus do not execute any code upon import.

To have python execute a directory add a __main__.py file to the directory. This is a very easy way to build small CLI programs.

Sample usage:
``` bash
python organizing\ larger\ programs/ hi
```

This can also be done via zip files.

#### Structuring python projects
Have the root directory (usually named after the project name) hold the dunder main file and licencing info.

Have a scripts directory for holding any potential utility scripts.

Have a directory named the same as the root directory to hold all source code. This should be a package. All sub-packages should follow. A tests directory should exist as well.

<img src="https://i.imgur.com/uhhwWbw.png" width=200>

Python modules act as singletons by default. Use the _something to indicate variables that should not be accessed directly. 