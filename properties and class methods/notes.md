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

