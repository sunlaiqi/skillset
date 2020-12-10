- [Singleton Class](#singleton-class)


# Singleton Class

The Singleton pattern ensures that a case has only one instance and ensures access to the instance through the application. It can be useful in cases where you have a “global” object with exactly one instance.

It should be noted that many people dislike the Singleton design pattern, even calling it “anti-pattern”. One reason for this is that it can interfere with unit testing.

This pattern restricts the instantiation of a class to one object. It is a type of creational pattern and involves only one class to create methods and specified objects.

It provides a global point of access to the instance created.

**How to implement a singleton class?**

The following program demonstrate the implementation of singleton class where is prints the instances created multiple times.

```python
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
            return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

s = Singleton()
print(s)
s = Singleton.getInstance()
print(s)
s = Singleton.getInstance()
print(s)
```
Output
The above program generates the following output -
```
<__main__.Singleton object at 0x7fdf31a2afa0>
<__main__.Singleton object at 0x7fdf31a2afa0>
<__main__.Singleton object at 0x7fdf31a2afa0>
```

The number of instances created are same and there is no difference in the objects listed in output.
