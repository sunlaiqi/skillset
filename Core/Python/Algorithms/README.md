- [Algorithms](#algorithms)
  - [Big O](#big-o)
    - [Complexity difference: O Ω Θ](#complexity-difference-o-ω-θ)
  - [Complexity of data structures](#complexity-of-data-structures)
    - [Data Structure](#data-structure)
    - [Algorithms](#algorithms-1)
  - [Recursion](#recursion)
    - [Base case and recursive case](#base-case-and-recursive-case)
    - [The stack](#the-stack)
  - [Hash tables](#hash-tables)
  - [Finding the shortest path](#finding-the-shortest-path)
    - [Queues](#queues)
    - [Implementing the graph](#implementing-the-graph)
  - [Dijkstra's algorithm](#dijkstras-algorithm)
    - [Terminology](#terminology)
- [Algorithm Cracking](#algorithm-cracking)
  - [Tips](#tips)
    - [Typical Class in Python](#typical-class-in-python)
      - [namedtuple](#namedtuple)
    - [% Modulus (reminder), // Floor division](#-modulus-reminder--floor-division)

# Algorithms

## Big O

Big O establishes a worst-case run time

Some common Big O run times
Here are five Big O run times that you’ll encounter a lot, sorted from fastest to slowest:
- **O(log n)**, also known as log time. Example: Binary search.
- **O(n)**, also known as linear time. Example: Simple search.
- **O(n * log n)**. Example: A fast sorting algorithm, like quicksort.
- **O(n^2)**. Example: A slow sorting algorithm, like selection sort.
- **O(n!)**. Example: A really slow algorithm, like the traveling salesperson.

### Complexity difference: O Ω Θ

- **O(f(n))** gives worst case complexity of given function/algorithm.
- **Ω(f(n))** (omega) gives best case complexity of given function/algorithm. 
- **Θ(f(n))** (theta) gives average case complexity of given function/algorithm.

## Complexity of data structures

### Data Structure

Data Structure              |Key Points
----------------------------|------------------------------------------------------------------
Primitive types             |Know how int, char, double, etc. are represented in memory and the primitive operations on them
Arrays                      |Fast access for element at an index, slow lookups (unless sorted) and insertions. Be comfortable with notions of iteration, resizing, partitioning, merging, etc.
Lists                       |Understand trade-offs with respect to arrays. Be comfortable with iteration, insertion, and deletion within singly and doubly linked lists. Know how to implement a list with dynamic allocation, and with arrays.
Stacks and queues           |Recognize where last-in first (stack) and first-in first-out (queue) semantics are applicable. Know array and linked list implementations.
Binary tree                 |Use for representing hierarchical data. Know about depth, height, leaves, search path, traversal sequences, successor/predecessor operations.
Heaps                       |Key benefit: O(1) lookup find-max, O(log n) insertion, and O(log n) deletion of max. Node and array representations. Min-heap variant.
Hash tables                 |Key benefit: O(1) insertions, deletion and lookups. Key disadvantages: not suitable for order-related queries; need for resizing; poor worst-case performance. Understand implementation using array of buckets and collision chains. Know hash functions for integers, strings, objects.
Binary search trees         |Key benefit: O(log n) insertions, deletions, lookups, find-min, find-max, successor, predecessor when tree is height-balanced. Understand node, fields, pointer implementation. Be familiar with notion of balance, and operations maintaining balance.

### Algorithms

Algorithm type          |Key points
------------------------|------------------------------------------------------------------------------------
Sorting                 |Uncover some structure by sorting the input
recursion               |If the structure of the input is defined in a recursive manner, design a recursive algorithm that follows the input definition.
Divide-and-conquer      |Divide the problem into two or more smaller independent sub-problems and solve the original problem using solutions to the subproblems.
Dynamic programming     |Compute solutions for smaller instances of a given problem and use these solutions to construct a solution to the problem. Cache for performance.
Greedy algorithms       |Compute a solution in stages, making choices that are locally optimum at each step; these choices are never undone.
Invariants              |Identify an invariant and use it to rule out potential solutions that are suboptimal/dominated by other solutions.
Graph modeling          |Describe the problem using a graph and solve it using an existing graph algorithm.



## Recursion


Recursion is used when it makes the solution clearer. There’s no performance benefit to using recursion; 
in fact, loops are sometimes better for performance. I like this quote by Leigh Caldwell on Stack Overflow: 
“Loops may achieve a performance gain for your program. Recursion may achieve a performance gain for your 
programmer. Choose which is more important in your situation!”

### Base case and recursive case

When you write a recursive function, you have to tell it when to stop recursing. That’s why every recursive function has two parts: the **base case**, and the **recursive case**. 
- **The recursive case** is when the function calls itself. 
- **The base case** is when the function doesn’t call itself again ... so it doesn’t go into an infinite loop.

### The stack

The call stack: OS uses stack to call a function, recursive functions use the call stack.
The stack has only two actions: push (insert) and pop (remove and read).

Using the stack is convenient because you don’t have to keep track of a pile of boxes yourself — the stack does it for you.
Using the stack is convenient, but there’s a cost: saving all that info can take up a lot of memory. Each of those function calls takes up some memory, and when your stack is too tall, that means your computer is saving information for many function calls. At that point, you have two options:
- You can rewrite your code to use a loop instead.
- You can use something called tail recursion. That’s an advanced recursion topic that is out of the scope of this book. It’s also only supported by some languages, not all.




## Hash tables

**Hash functions**
A hash function is a function where you put in a string and you get back a number. In technical terminology, we’d say that a hash function “maps strings to numbers.” 

Put a hash function and an array together, and you get a data structure called 
a **hash table**. 

Hash tables in Python are called dictionaries
`book = dict() or book = {}`
A hash table has keys and values. In the book hash, the names of produce are the keys, and their prices are the values. A hash table maps keys to values.

Also, `set`, `collections.defaultdict` and `collections.Counter` are hash table based data structure.
The difference between `set` and the other three is that is `set` simply stores keys, whereas the others store `key-value` pairs. All have the property that they do not allow for **duplicate keys**, unlike, for example, list.


DNS uses hash tables for mapping hostname to IP address. Hash tables are used for caching for websites.

The most important operations for set are `s.add(42)`, `s.remove(42)`, `s.discard(123)`, `x in s` as well as `s <= t `(is s a subset of t), and `s - t` (elements in s that are not in t).

Note that the built-in `hash()` function can greatly simplify the implementation of a hash function for a user-defined class, i.e., implementing `__hash__( self)`.


**Use cases**:
Using hash tables for lookups, like phone book
Preventing duplicate entries
Using hash tables as a cache

**Collisions**

The simplest one is this: if multiple keys map to the same slot, start a linked list at that slot.

To avoid collisions, you need
• A low load factor
• A good hash function
```
load factor = number of items in hash table / total number of slots 
```
Load factor measures how many empty slots remain in your hash table.

Having a load factor greater than 1 means you have more items than slots in your array. Once the load factor starts to grow, you need to add more slots to your hash table. This is called **resizing**.
A good rule of thumb is, resize when your load factor is greater than **0.7**.
Resizing is expensive, and you don’t want to resize too often. But averaged out, hash tables take O(1) even with resizing.

A good hash function
A good hash function distributes values in the array evenly.

If the hash function does a good job of spreading objects across the underlying array and take O(1) time to compute, on average, lookups, insertions, and deletions have O(1 + n/m) time complexity, where n is the number of objects and m is the length of array.

**Performance**

In the average case, hash tables take `O(1)` for everything. O(1) is called constant time. 
Getting an item out of an array takes constant time. It doesn’t matter how big your array is; it takes the same amount of time to get an element. 
Look at the average case for hash tables. Hash tables are as fast as arrays at searching (getting a value at an index). And they’re as fast as linked lists at inserts and deletes.


## Finding the shortest path

As a recap, these are the two questions that breadth-first search can answer for you:
- Question type 1: Is there a path from node A to node B? 
- Question type 2: What is the shortest path from node A to node B? 

The way breadth-first search works, the search radiates out from the starting point. So you’ll check first-degree connections before second-degree connections. 

So you need to search people in the order that they’re added. There’s a data structure for this: it’s called a queue.

### Queues

Queues are similar to stacks. You can’t access random elements in the queue. 
Instead, there are two only operations, **enqueue** and **dequeue**.

### Implementing the graph

How do you express a relationship like “you -> bob”? Luckily, you know a data structure that lets you express relationships: a hash table!
Here’s how you’d write it in Python:
```python
graph = {}
graph[“you”] = [“alice”, “bob”, “claire”]
```

This is called a directed graph — the relationship is only one way. So you are Bob’s neighbor, but Bob isn’t your neighbor. An undirected graph doesn’t have any arrows, and both nodes are each other’s neighbors.

Make a queue to start. In Python, you use the double-ended queue (deque) function for this:
```python
from collections import deque
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # This array is how you keep track of which people you’ve searched before.
    searched = [] 
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if not person in searched:
            # person_is_seller should be defined up front.
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                # Make this person as searched
                searched.append(person)
    return False

search(“you”)
```

Running time
Breadth-first search takes `O(number of people + number of edges)`, and it’s more commonly written as O(V+E) (V for number of vertices, E for number of edges).



## Dijkstra's algorithm

in Dijkstra’s algorithm, you assign a number or **weigh**t to each segment. Then Dijkstra’s algorithm finds the path with the smallest total weight.

To recap, Dijkstra’s algorithm has four steps:
1. Find the cheapest node. This is the node you can get to in the least amount of time.
2. Check whether there’s a cheaper path to the neighbors of this node. If so, update their costs.
3. Repeat until you’ve done this for every node in the graph.
4. Calculate the final path. 

### Terminology

When you work with Dijkstra’s algorithm, each edge in the graph has a number associated with it. These are called **weights**.

A graph with weights is called a **weighted graph**. A graph without weights is called an **unweighted graph**.

To calculate the shortest path in an unweighted graph, use breadth-first search. To calculate the shortest path in a weighted graph, use Dijkstra’s algorithm. 

Graphs can also have cycles. It means you can start at a node, travel around, and end up at the same node. An undirected graph means that both nodes point to each other. 

That’s a cycle!

Dijkstra’s algorithm only works with directed acyclic graphs, called DAGs for short.



# Algorithm Cracking 

## Tips

### Typical Class in Python

Use **collections.namedtuples** extensively for structured data-these are more readable than dictionaries, lists, and tuples, and less verbose than classes.
Use the following constructs to write simpler code: aIl () and any(), list comprehension, map(), functools. reduce() and zip(), and enumerate().
The following functions from the itertools module are very useful in diverse contexts: groupby(), accumulate(), product(), and combinations().

#### namedtuple
```python
from collections import namedtuple 

websites = [
('Sohu', 'http://www.google.com/', u'张朝阳'), 
('Sina', 'http://www.sina.com.cn/', u'王志东'), 
('163', 'http://www.163.com/', u'丁磊')
]
Website = namedtuple('Website', ['name', 'url', 'founder'])
for website in websites:
    website = Website._make(website) 
    print(website)
```

In addition to the methods inherited from tuples, named tuples support three additional methods and one attribute. To prevent conflicts with field names, the method and attribute names start with an underscore.

classmethod 
`somenamedtuple._make(iterable)`
Class method that makes a new instance from an existing sequence or iterable.
```python
>>> t = [11, 22]
>>> Point._make(t)
Point(x=11, y=22)
```

`somenamedtuple._asdict()`

Return a new OrderedDict which maps field names to their corresponding values:
```python
>>> p = Point(x=11, y=22)
>>> p._asdict()
OrderedDict([('x', 11), ('y', 22)])
```

`somenamedtuple._replace(**kwargs)`
Return a new instance of the named tuple replacing specified fields with new values:
```python
>>> p = Point(x=11, y=22)
>>> p._replace(x=33)
Point(x=33, y=22)
```
To convert a dictionary to a named tuple, use the double-star-operator (as described in Unpacking Argument Lists):
```python
>>> d = {'x': 11, 'y': 22}
>>> Point(**d)
Point(x=11, y=22)
```

### % Modulus (reminder), // Floor division
```python
# round(number, digits), ex: 
round(5.76543, 2)   # = 5.77
print(5 % 2)    # = 1
print(5 // 2)   # = 2
```

