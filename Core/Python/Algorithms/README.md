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

## Selection sort

```python
# To sort the array from smallest to largest
# e.g. [5, 3, 6, 2, 10] => [2, 3, 5, 6, 10]
# First define a function to find the smallest

def find_smallest_index(arr):
    smallest_index = 0
    smallest_value = arr[0]
    for i in range(len(arr)):
        smallest_index = i if smallest_value > arr[i] else smallest_index
        smallest_value = arr[smallest_index]
    return smallest_index

def select_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        print(find_smallest_index(arr))
        new_arr.append(arr.pop(find_smallest_index(arr)))
    return new_arr

print(select_sort([5, 3, 6, 2, 10]))

```
## Bubble Sort

```python
def bubble_sort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

```

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

## Quicksort

Quicksort steps:
1. Pick a pivot.
2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
3. Call quicksort recursively on the two sub-arrays.
```python
def quicksort(array):
    if len(array) < 2:
        return array # Base case: arrays with 0 or 1 element are already “sorted.”
    else:
        pivot = array[0] # Recursive case
        less = [i for in in array[1:] if i <= pivot]
        greater = [i for in in array[1:] if i > pivot ]

        return quicksort(less) + pivot + quicksort(greater)
```

There’s another sorting algorithm called **merge sort**, which is O(nlogn). Much faster! Quicksort is a tricky case. In the worst case, quicksort takes O(n^2) time. It’s as slow as selection sort! But that’s the worst case. In the average case, quicksort takes O(nlogn) time. 

But sometimes the constant can make a difference. Quicksort versus merge sort is one example. Quicksort has a smaller constant than merge sort. So if they’re both O(nlogn) time, quicksort is faster. 
And quicksort is faster in practice because it hits the average case way more often than the worst case. Well, guess what? I’m here to tell you that the best case is also the average case. If you always choose a random element in the array as the pivot, quicksort will complete in `O(nlogn)` time on average. Quicksort is one of the fastest sorting algorithms out there, and it’s a very good example of D&C.


## Hash tables

Hash functions
A hash function is a function where you put in a string and you get back a number. In technical terminology, we’d say that a hash function “maps strings to numbers.” 

Put a hash function and an array together, and you get a data structure called 
a hash table. 

A hash table has keys and values. In the book hash, the names of produce are the keys, and their prices are the values. A hash table maps keys to values.

**Use cases**:
Using hash tables for lookups, like phone book
Preventing duplicate entries
Using hash tables as a cache

**Collisions**

The simplest one is this: if multiple keys map to the same slot, start a linked list at that slot.

**Performance**

In the average case, hash tables take O(1) for everything. O(1) is called constant time. 
Getting an item out of an array takes constant time. It doesn’t matter how big your array is; it takes the same amount of time to get an element. 
Look at the average case for hash tables. Hash tables are as fast as arrays at searching (getting a value at an index). And they’re as fast as linked lists 
at inserts and deletes.

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

## Breadth-first search

The algorithm to solve a shortest-path problem is called breadth-first search.

### Graphs

What is a graph?
A graph models a set of connections.
Each graph is made up of **node**s and *edges*.
A node can be directly connected to many other nodes. Those nodes are called 
its neighbors.

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
To calculate the shortest path in an unweighted graph, use breadth-first search. 
To calculate the shortest path in a weighted graph, use Dijkstra’s algorithm. 
Graphs can also have cycles. It means you can start at a node, travel around, and end up at the same node. An undirected graph means that both nodes point to each other. 
That’s a cycle!
Dijkstra’s algorithm only works with directed acyclic graphs, called DAGs for short.














