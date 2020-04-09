import sys

from some_package import SomeClass

print("Do something")

try:
    SomeClass().print(sys.argv[1])
finally:
    print("Done")
