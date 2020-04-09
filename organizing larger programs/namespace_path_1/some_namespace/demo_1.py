class dummy_demo_1():
    def __init__(self):
        print(f"{self.__class__.__name__} init")


    def print(self, text):
        print(f"{self.__class__.__name__} printing: {text}")