class MyDescriptor: 
    
    def __init__(self, value=0):
        self.value = value

    def __get__(self, obj, type=None): 
        print("getter method called") 
        return self.value
    
    def __set__(self, obj, value): 
        print(f"setter method called for {value}") 
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError(f"The value {value} is invalid")
        self.value = value
class Foo:
    age = MyDescriptor()

mark = Foo()
print(mark.age)
mark2 = Foo()
print(mark.age)
print(mark2.age)
mark.age = 8
print(mark.age) 
print(mark2.age)