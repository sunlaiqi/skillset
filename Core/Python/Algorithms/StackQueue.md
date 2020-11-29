- [Stacks and Queues](#stacks-and-queues)
  - [Stacks boot camp](#stacks-boot-camp)
  - [Know your stack libraries](#know-your-stack-libraries)
  - [Implement a stack with max/min API](#implement-a-stack-with-maxmin-api)


# Stacks and Queues

## Stacks boot camp

It’s useful to create reverse iterator for sequences.

```python
def print_linked_list_in_reverse(head): 
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next 
        while nodes:
            print(nodes.pop())
```
## Know your stack libraries

- **s.append(e)** pushes an element onto the stack. Not much can go wrong with a call to push.
- **s [-1]** will retrieve, but does not remove, the element at the top of the stack. 
- **s.pop()** will remove and return the element at the top of the stack.
- **len(s) == 0** tests if the stack is empty.
- When called on an empty list `s`, both `s[-1]` and `s.pop()` raise an `IndexError` exception.

## Implement a stack with max/min API

Here is the min solution:

Problem:
Stack Min: How would you design a stack which, in addition to push and pop,
has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time. 

Solution 1
```python
class StackWithMin: 
    stack_list = [] 
    min_list = []
    def push(self, data):
        self.stack_list.append(data) 
        if len(self.min_list) > 0:
            if self.min_list[-1] > data: 
                self.min_list.append(data)
        else: 
            self.min_list.append(data)

    def pop(self):
        if len(self.stack_list) > 0:
            data = self.stack_list.pop() 
            if self.min_list[-1] == data:
                self.min_list.pop()
    
    def min(self):
        if len(self.min_list) == 0:
            print("Stack is Empty!")
            return
        
        return self.min_list[-1]
    
    def __repr__(self):
        return str(self.stack_list + ["|"] + self.min_list)

A = StackWithMin()
A.push(9)
A.push(4)
A.push(23)
A.push(9)
A.push(6)
A.push(1)

print(A)
print(A.min())
# [9, 4, 23, 9, 6, 1, '|', 9, 4, 1]
# 1

```