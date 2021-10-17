- [Arrays (List)](#arrays-list)
  - [Array Boot Camp](#array-boot-camp)
  - [Problems & Solutions](#problems--solutions)
    - [Reorder: Even entries appears first](#reorder-even-entries-appears-first)
    - [First half equals second half](#first-half-equals-second-half)
  - [Top tips for array](#top-tips-for-array)
  - [Know your array libraries](#know-your-array-libraries)
    - [Know how to instantiate a 2D array](#know-how-to-instantiate-a-2d-array)
    - [Understand how copy works](#understand-how-copy-works)
    - [Copy vs deep copy](#copy-vs-deep-copy)
    - [binary search for sorted lists](#binary-search-for-sorted-lists)
    - [Flatten a 2D list](#flatten-a-2d-list)
  - [functools module](#functools-module)
    - [Calculate b based integer in string to a decimal integer](#calculate-b-based-integer-in-string-to-a-decimal-integer)
    - [functools.cache(user_function)](#functoolscacheuser_function)
  - [Array manipulation](#array-manipulation)
    - [how to calculate max number for overlap array???](#how-to-calculate-max-number-for-overlap-array)
    - [Use deque over list on stack](#use-deque-over-list-on-stack)
    - [Use Counter to get the frequency of occurrences](#use-counter-to-get-the-frequency-of-occurrences)
    - [How to sort a dict by value](#how-to-sort-a-dict-by-value)
    - [The Dutch national flag problem](#the-dutch-national-flag-problem)
    - [Increment an arbitrary-precision integer](#increment-an-arbitrary-precision-integer)
    - [Multiply two arbitrary-precision integer](#multiply-two-arbitrary-precision-integer)


# Arrays (List) 


## Array Boot Camp


## Problems & Solutions

### Reorder: Even entries appears first


**Problem:** 
Your input is an array of integers, and you have to reorder its entries so that the even entries appear fist.

**Solution:**
When working with arrays you should take advantage of the fact that you can operate efficiently on **both ends**. For this problem, we can partition the array into three subarrays: **Even**, **Unclassified**, and **Odd**, appearing in that order. 
Initially `Even` and `Odd` are empty, and `Unclassified` is the entire array. We iterate through `Unclassified`, moving its elements to the boundaries of the `Even` and `Odd` subarrays via `swaps`, thereby expanding `Even` and `Odd`, and shrinking `Unclassifie`d.

```python
def even_odd(A):
    next_even, next_odd = 0, len(A) - 1 
    while next_even < next_odd:
        if A[next_even] % 2 == 0: 
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
```

The time complexity is *O(n)* and space complexity is *O(1)*

### First half equals second half

```python
def first_second(A):
    all_sum = sum(A)
    temp_sum = 0
    for i in range(len(A)):
        temp_sum += A[i]
        if temp_sum == all_sum - temp_sum:
            print(f"Found equal point: {i}")
            return i
    print(f"THe array could not be splited equally.")
```

Use `enumerate()`:
```python
def first_second(A):
    all_sum = sum(A)
    temp_sum = 0
    for i, num in enumerate(A):
        temp_sum += num
        if temp_sum == all_sum - temp_sum:
            print(f"Found equal point: {i}")
            return i
    print(f"THe array could not be splited equally.")
```


## Top tips for array

Array problems often have simple brute force solutions that use O(n) space, but there are subtler solutions that use the array itself to reduce space complexity to O(1).

Filling an array from the front is slow, so see if it's possible to write values from the back. Instead of deleting an entry (which requires moving all entries to its left), consider overwriting it.

When dealing with integers encoded by an array, consider processing the digits from the back of the array. Alternately, reverse the array so the least-significant digit is the first entry.

Be comfortable with writing code that operates on subarrays
It's incredibly easy to make off-by-1 errors when operating on arrays-reading. Past the last element of an array is a common error which has catastrophic consequences.

Don't worry about preserving the integrity of the array (sortedness, keeping equal entries together, etc.) until it is time to return.

An array can serve as a good data structure when you know the distribution of the elements in advance. For example, a Boolean array of length W is a good choice for representing a subset of {0,1,...,W-1} (When using a Boolean array to represent a subset of {1,2,3,.. . ,n}, allocate an array of size n+1 to simplify indexing.).

When operating on 2D arrays, use parallel logic for rows and for columns. Sometimes it's easier to simulate the specification, than to analytically solve for the result. For example, rather than writing a formula for the i-th entry in the spiral order for an `n x n` matrix, just compute the output from the beginning.

## Know your array libraries

### Know how to instantiate a 2D array

### Understand how copy works

The difference between `B = A` and `C = list(A)` 

```python
>>> A is B
True
>>> A == B
True
>>> A == C
True
>>> A is C
False
```

### Copy vs deep copy

**Shallow copy**

```python
new_list = list(original_list) 
new_dict = dict(original_dict) 
new_set = set(original_set)
```
These only create shallow copies.

A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original. In essence, a shallow copy is only *one level deep*. The copying process does not recurse and therefore won’t create copies of the child objects themselves.

A shallow copy is independent from the original, but just at one level. 
```python
>>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> ys = list(xs) # Make a shallow copy Or
import copy
ys = copy.copy(xs)
>>> xs
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> ys
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> xs.append(['new sublist'])
>>> xs
[[1, 2, 3], [4, 5, 6], [7, 8, 9], ['new sublist']]
>>> ys
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> xs[1][0] = 'X'
>>> xs
[[1, 2, 3], ['X', 5, 6], [7, 8, 9], ['new sublist']]
>>> ys
[[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
# The children were not copied. It still contains references to the original child objects.
```

**Deep copy**

A deep copy makes the copying process **recursive**. It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original. Copying this way walks the whole object tree to create a fully independent clone of the original object and all of its children.

```python
>>> import copy
>>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
>>> zs = copy.deepcopy(xs)
```

### binary search for sorted lists 

(bisect.bisect(A,6), 
bisect.bisect-left(A,6), and 
bisect.bisect_right(A,6)), 
A.reverse() (in-place), 
reversed(A) (returns an iterator), 
A.sort() (in-place), 
sorted(A) (returns a copy), 
del A[i] (deletes the i-th element), and 
del A[i: j] (removes the slice).
A[::-1] reverse the list
A[k:] + A[:k] rotate A by k to the left. 
B =A[:] does a shallow copy of A to B

### Flatten a 2D list

```python
>>> M = [['a', 'b', 'c'], ['d', 'e', ‘f']]
>>> N = [x for row in M for x in row]
['a', 'b', 'c', 'd', 'e', 'f ']
```

## functools module

The functools module is for higher-order functions: functions that act on or return other functions.

### Calculate b based integer in string to a decimal integer

Usually, it’s better to reduce to get the sum by using `reduce` function in `functools` lib.
E.g. the `x` is a string, which includes an integer, then the function would be:

```python
import functools
x = “x1x2x3x4...xn”
functools.reduce(lambda result, a: result * b + int(a), x, 0)
```

The `functools.reduce(function, iterable[, initializer])` function is used to apply a particular function passed in its argument to all of the list elements mentioned in the `iterable` passed along.

Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, 
`reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])` calculates `((((1+2)+3)+4)+5)`. 
The left argument, `x`, is the *accumulated value* and the right argument, y, is the *update value* from the iterable. If the optional `initializer` is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If `initializer` is not given
and iterable contains only one item, the *first item* is returned.

```python
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it) 
    else:
        value = initializer 
    for element in it:
        value = function(value, element) 
    return value
```


### functools.cache(user_function)

Simple lightweight unbounded function cache. Sometimes called “memoize”.

## Array manipulation 

### how to calculate max number for overlap array???

**Problem:**
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros . Your list of queries is as follows:
```
a b k
1 5 3 
4 8 7 
6 9 1
```
Add the values of between the indices and inclusive: 
```
index-> 1 2 3 4 5 6 7 8 9 10
[0,0,0, 0, 0,0,0,0,0, 0] 
[3,3,3, 3, 3,0,0,0,0, 0] 
[3,3,3,10,10,7,7,7,0, 0] 
[3,3,3,10,10,8,8,8,1, 0]
```
The largest value is after all operations are performed.

**Solution 1:** 
O(n*m) too slow
```python
# n = length of the array
# queries = operation array
def arrayManipulation(n, queries):
    x = [0] * n
    m = len(queries) 
    for i in range(m):
        for j in range(queries[i][0]-1, queries[i][1]): 
            x[j] += queries[i][2]
    return max(x)
```

**Solution 2:** 
O(n+m), faster
```python
def arrayManipulation(n, queries): 
    x = [0] * n
    m = len(queries)
    for i in range(m):
        # Add k to array’s (a-1) location, i.e. the first location for k 
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        x[a -1] += k
        if b < n: # if b is the last location the array, no need to -k
            # Out of a ~ b, so -k
            x[b] -= k 
    max_num = 0
    sum = 0 
    for j in x:
        sum += j
        if sum > max_num:
            max_num = sum 
    return max_num
```

### Use deque over list on stack

Deque provides an *O(1)* time complexity for `append` and `pop` operations as compared to list which provides *O(n)* time complexity.

Operations on deque :
1. **append()** :- This function is used to insert the value in its argument to the right end of deque.
2. **appendleft()** :- This function is used to insert the value in its argument to the left end of deque.
3. **pop()** :- This function is used to delete an argument from the right end of deque.
4. **popleft()** :- This function is used to delete an argument from the left end of deque.
5. **index(ele, beg, end)** :- This function returns the first index of the value mentioned in arguments, starting searching from `beg` till `end` index.
6. **insert(i, a)** :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
7. **remove(a)** :- This function removes the first occurrence of value mentioned in arguments.
8. **count(a)** :- This function counts the number of occurrences of value mentioned in arguments.
9. **extend(iterable)** :- This function is used to add multiple values at the right end of deque. The argument passed is an iterable.
10. **extendleft(iterable)** :- This function is used to add multiple values at the left end of deque. The argument passed is an iterable. Order is reversed as a result of left appends.
11. **reverse()** :- This function is used to reverse order of deque elements.
12. **rotate(k)** :- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to left. Else rotation is to right.

### Use Counter to get the frequency of occurrences

**Problem**:
Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. 
Given a string , determine if it is valid. If so, return YES, otherwise return NO.
For example, if `s = abc`, it is a valid string because frequencies are {a:1, b:1, c:1}. So is `s = abcc` because we can remove one c and have 1 of each character in the remaining string. If `s = abccc` however, the string is not valid as we can only remove 1 occurrence of c. That would leave character frequencies of {a:1, b:1, c:2}.

**Solution**:
```python
from collections import Counter

def isValid(s):
    if len(s) <= 3:
        return 'YES'
    s_dict = dict(Counter(s))
    # counter_f = {frequence: frequence count, .....}
    counter_f = dict(Counter([value for value in s_dict.values()])) 
    print(counter_f)
    if len(counter_f) > 2:
        return 'NO'
    elif len(counter_f) == 1:
        return 'YES' 
    else:   # when counter_f == 2, 2 difference occurrences. 
        frequence = [i for i in counter_f.keys()] 
        min_c = counter_f[min(frequence)]   # times at low occurrence
        max_c = counter_f[max(frequence)]   # times at high occurrence
        if min_c == 1 and min(frequence) == 1:  # high occurrence only could appear 1 time
            return 'YES'
        elif max_c == 1 and (max(frequence) - min(frequence)) == 1:
            return 'YES'
        else:
            return 'NO' ## ???

A = 'aabbccc'
print(isValid(A))
#{2: 2, 3: 1}
# YES

```

### How to sort a dict by value

```python
# How to sort a Python dict by value
# (== get a representation sorted by value)
>>> xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
>>> sorted(xs.items(), key=lambda x: x[1]) 
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
# Or:
>>> import operator
>>> sorted(xs.items(), key=operator.itemgetter(1)) 
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```

### The Dutch national flag problem

**Problem:**

Write a program that takes an array A and an index i into A, and rearranges the elements such that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot, followed by elements greater than the pivot.

**Solution:**
```python
RED, WHITE, BLUE = range(3)
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # # bottom group: A[:smaller].
    # # middle group: A[smaller:equal].
    # # unclassified group: A[equal: larger] .
    # # top group: A[larger: ]
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element 
    while equal < larger:
    # A[equal] is the incoming unclassified element, 
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller , equal = smaller + 1, equal + 1 
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot.
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal] 
    return A

A = [1, 2,4,6,8,5,3,2,1,10,9,12] 
print(dutch_flag_partition(5, A))
# [1, 2, 4, 1, 2, 3, 5, 8, 10, 9, 12, 6]
```

Each iteration decreases the size of unclassified by 1, and the time spent with each iteration is *O(1)*, implying the time complexity is *O(n)*. The space complexity is clearly *O(1)*.

### Increment an arbitrary-precision integer

**Problem:**
Write a program which takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1. For example, if the input is `(1,2,9)` then you should update the array to `(1,3,0)`. Your algorithm should work even if it is implemented in a language that has finite-precision arithmetic.

**Solution:**
```python
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10: 
            break
        A[i] = 0
        A[i - 1] += 1 
    if A[0] == 10:
        # There is a carry-out, so we need one more digit to store the result 
        # A slick way to do this is to append a 0 at the end of the array
        # and update the first entry to 1.
        A[0] = 1
        A.append(0)
    return A

A = [1,2,3,9]
plus_one(A)
print(A)
# [1, 2, 4, 0]
```

### Multiply two arbitrary-precision integer

**Problem**:
multiply two arbitrary-precision integers
Certain applications require arbitrary precision arithmetic. One way to achieve
this is to use arrays to represent integers, e.g., with one digit per array
entry with the most significant digit appearing first, and a negative leading digit denoting a negative integer. For example, (1,9,3,7,0,7,7,2,1) represents 193707721 and (-7,6,1,8,3,8,2,5,7,2,8,7) represents -761838257287.

**Solution:**
```python
def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1 
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2)) 
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))): 
            result[i + j + 1] += num1[i] * num2[j] 
            result[i + j] += result[i + j + 1] // 10 
            result[i + j + 1] %= 10
    # remove the leading zeroes
    # len(result) in next is a default if result is [0]
    # next(iterator, default)
    # result[len(result):] == []
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]

num1 = [1,5]
num2 = [1,5]

print(multiply(num1, num2))
# [2, 2, 5]
```
