def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start decoration.")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
class MyClass:
    def __init__(self, x="Hello!"):
        self.x = x
        print(self.x)
    def hello(self, y):
        print(y)
    

a = MyClass()
a.hello("This is fun!")
b = MyClass("Ni Hao!")
b.hello("Zhen Hao Wan!")
