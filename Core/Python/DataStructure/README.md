# Data Structure

- Dictionary
- List
- Dequeue
- Tree
- Graph

### Array

Array is a container which can hold a fix number of items and these items should be of the same type. Most of the data structures make use of arrays to implement their algorithms. 
Array is created in Python by importing array module to the python program. Then the array is declared as shown eblow.
```python
from array import *
arrayName = array(typecode, [Initializers])
```
Typecode    |	Value
---         |   ---
b   |	Represents signed integer of size 1 byte
B	|   Represents unsigned integer of size 1 byte
c   |	Represents character of size 1 byte
i   |	Represents signed integer of size 2 bytes
I   |	Represents unsigned integer of size 2 bytes
f   |	Represents floating point of size 4 bytes
d   |	Represents floating point of size 8 bytes

```python
from array import *
array1 = array('i', [10,20,30,40,50])
for x in array1:
    print(x)
```

#### Accessing Array Element

We can access each element of an array using the index of the element. The below code shows how
```python
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1[0])
print (array1[2])
array1.insert(1,60)
array1.remove(40)
print (array1.index(40))
array1[2] = 80
```

### List

**Delete List Elements**

To remove a list element, you can use either the del statement if you know exactly which element(s) you are 
deleting or the remove() method if you do not know. For example −
```python
#!/usr/bin/python

list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]
print("After deleting value at index 2 : ")
print(list1)
```

### Arrays and linked lists

- With an array, all your elements are stored right next to each other.
- With a list, elements are strewn all over, and one element stores the address of the next one.
- Arrays allow fast reads.
- Linked lists allow fast inserts and deletes.

### tuple

The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
To write a tuple containing a single value you have to include a comma, even though there is only one value. Otherwise, it will be evaluated as a single value.

tup1 = (50,);

### dictionary

Properties of Dictionary Keys:

- (a) More than one entry per key not allowed. Which means no duplicate key is allowed. When duplicate keys encountered during assignment, the last assignment wins. 
- (b) Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed. 

### set

Mathematically a set is a collection of items not in any particular order. A Python set is similar to this mathematical definition with below additional conditions.
- The elements in the set cannot be duplicates.
- The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.
- There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

#### Accessing Values in a Set

We cannot access individual values in a set. We can only access all the elements together as shown above. But we can also get a list of individual elements by looping through the set.
```python 
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
for d in Days:
	print(d)

Days.add("Sun")
Days.discard("Sun")
```

#### Union of Sets

The union operation on two sets produces a new set containing all the distinct elements from both the sets. 
In the below example the element “Wed” is present in both the sets.
```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)

#{'Sun', 'Fri', 'Mon', 'Wed', 'Sat', 'Tue', 'Thu'}

# Intersection of Sets
AllDays = DaysA & DaysB
print(AllDays)

# {'Wed'}

# Difference of Sets
AllDays = DaysA - DaysB

```
#### Compare Sets

We can check if a given set is a subset or superset of another set. The result is True or False depending on the elements present in the sets.

```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)
```
When the above code is executed, it produces the following result.

True
True
