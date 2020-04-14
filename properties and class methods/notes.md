## Properties and class methods

The ```@classmethod``` decorator can be used on methods to gain access to the class definition.

```Python

class Something:

    next_serial = 101

    @classmethod
    def _get_next_serial(cls):
        serial = cls.next_serial
        cls.next_serial += 1
        return serial

    def __init__(self):
        self.serial = Something._get_next_serial()

```

Python handles encapsulation via the ```@property``` decorator. Use a _ prefix to annotate properties.

```Python
class Something:

    def __init(self):
        self._some_property = 10

    @property
    def some_property(self):
        return self._some_property

    @some_property.setter
    def some_property(self, value):
        # Add validation logic here
        self._some_property = value
```