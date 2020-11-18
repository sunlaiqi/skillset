- [Class and Object](#class-and-object)
  - [Namespace](#namespace)
  - [Scope](#scope)
  - [global/nonlocal statements](#globalnonlocal-statements)
    - [Scopes and Namespaces Example](#scopes-and-namespaces-example)
  - [Class Definition Syntax](#class-definition-syntax)
    - [Class Objects](#class-objects)
    - [Instance Objects](#instance-objects)
    - [Method Objects](#method-objects)
    - [Class and Instance Variables](#class-and-instance-variables)
    - [Name mangling](#name-mangling)

# Class and Object

Python classes provide all the standard features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name. Objects can contain arbitrary amounts and kinds of data.

## Namespace

A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries. Examples of namespaces are: the set of built-in names (containing functions such as `abs()`, and built-in exception names); the global names in a module; and the local names in a function invocation. In a sense the set of attributes of an object also form a namespace. The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces; for instance, two different modules may both define a function maximize without confusion — users of the modules must prefix it with the module name.
Namespaces are created at different moments and have different lifetimes. The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits. The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called `__main__`, so they have their own global namespace. (The built-in names actually also live in a module; this is called builtins.)
The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function. 

## Scope

A scope is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

## global/nonlocal statements
The global statement can be used to indicate that particular variables live in the global scope and should be rebound there; the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound there.

A special quirk of Python is that – if no global or nonlocal statement is in effect – assignments to names always go into the innermost scope. Assignments do not copy data — they just bind names to objects. The same is true for deletions:the statement *del x* removes the binding of x from the namespace referenced by the local scope. In fact, all operations that introduce new names use the local scope: in particular, import statements and function definitions bind the module or function name in the local scope.

### Scopes and Namespaces Example
This is an example demonstrating how to reference the different scopes and namespaces, and how global and nonlocal affect variable binding:
```python
def scope_test(): 
    def do_local():
        spam = "local spam"
    def do_nonlocal(): 
        nonlocal spam
        spam = "nonlocal spam"
    def do_global(): 
        global spam
        spam = "global spam"

spam = "test spam"
do_local()
print("After local assignment:", spam) do_nonlocal()
print("After nonlocal assignment:", spam) do_global()
print("After global assignment:", spam)
scope_test()
print("In global scope:", spam)
```
The output of the example code is:
```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```
Note how the *local* assignment (which is default) didn’t change scope_test’s binding of spam. The *nonlocal* assignment changed scope_test’s binding of spam, and the *global* assignment changed the module-level binding.
You can also see that there was no previous binding for spam before the *global* assignment.

## Class Definition Syntax
**Official definition**:
A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class.

```python
class ClassName: 
    <statement-1>
    .
    .
    .
    <statement-N>
```
When a class definition is left normally (via the end), a class object is created. Rememer, everything in Python is object.

### Class Objects

Class objects support two kinds of operations: attribute references and instantiation.
Attribute references use the standard syntax used for all attribute references in Python: obj.name. Valid attribute names are all the names that were in the class’s namespace when the class object was created. 
Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class. 
x = MyClass()
creates a new instance of the class and assigns this object to the local variable x.

### Instance Objects
The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names: data attributes and methods.

### Method Objects

Instance method objects have attributes, too: `m.__self__` is the instance object with the method m(), and `m. __func__` is the function object corresponding to the method.

### Class and Instance Variables

Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class. 
Correct design of the class should use an instance variable instead.
Each value is an object, and therefore has a class (also called its type). It is stored as `object.__class__`.

### Name mangling
Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped.