- [Strings](#strings)
  - [Strings Boot Camp](#strings-boot-camp)
  - [Know your string libraries](#know-your-string-libraries)
  - [Top tips for strings](#top-tips-for-strings)
  - [String Manipulationg](#string-manipulationg)
    - [Palindromic (回文) string](#palindromic-回文-string)
    - [Making Anagrams](#making-anagrams)
    - [Find anagrams](#find-anagrams)
    - [Interconvert strings and integers](#interconvert-strings-and-integers)
    - [Base conversion](#base-conversion)

# Strings

A string can be viewed as a special kind of array, namely one made out of characters.

## Strings Boot Camp

## Know your string libraries

The key operators and functions on strings: 
```python
s.strip()
s.startswith(prefix)
s.endswith(suffix)
s.split(‘,’)
3 * '01'
','.join(('Gauss', 'Prince of Hathematicians', '1777-1855'))
s.lower()
'Name {name}, Rank {rank}'.format(name='Archimedes', rank=3)
```

## Top tips for strings

It's important to remember that strings are immutable 
- operations like `s = s[1:]` or `s += ' 123'` imply creating a **new array of characters** that is then assigned back to `s`. 
- This implies that concatenating a single character `n` times to a string in a `for loop` has *O(n**2)* time complexity.
- Similar to arrays, string problems often have simple *brute-force* solutions that use *O(n)* space solution, but subtler solutions that use the string itself to reduce space complexity to *O(1)*.
- Understand the implications of a string type which is immutable, e.g., the need to allocate a new string when concatenating immutable strings. 
- Know alternatives to immutable strings, e.g., a list in Python.
- Updating a mutable string from the front is slow, so see if it's possible to write values from the back.


## String Manipulationg

### Palindromic (回文) string

A string is said to be a palindrome if the string read from left to right is equal to the string read from right to left. 

Rather than creating a new string for the reverse of the input string, it traverse the input
string forwards and backwards, thereby saving space.
```python
def is_palindromic(s):
    # Note that s[~i] for i in [0, len(s) -1] is s[-(i + 1)] 
    return all(s[i] == s[~i] for i in range(len(s) // 2))

def simple_reverse(s): 
    return s == s[::-1]

def double_palindromic(s):
    l = len(s) // 2
    for i, value in enumerate(s):
        if value != s[-(i + 1)]:
            return False
    return True

s = "abcdcba"
print(is_palindromic(s)) 
print(simple_reverse(s))
print(double_palindromic(s))
s = "afdgdgage"
print(is_palindromic(s)) 
print(simple_reverse(s))
print(double_palindromic(s))
# True
# True
# True
# False
# False
# False
```

**From both ends of the string**

```python
def is_palindrome(s):
    # i moves forward, and j moves backward 
    i, j = 0, len(s) - 1
    while i < j:
    # i and j both skip non-alphanumeric characters, 
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True
```
we spend *O(1)* per character, so the time complexity is *O(n)*, where `n` is the length of `s`

**Use collections.Counter**

```python
import collections
def can_form_palindrome(s):
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1
```

The time complexity is *O(n)*, where `n` is the length of the string. The space complexity is *O(c)*, where `c` is the number of distinct characters appearing in the string.


### Making Anagrams

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.

Given two strings, and , that may or may not be of the same length, determine the minimum number of character deletions required to make and anagrams. Any characters can be deleted from either of the strings.

```python
def build_dict(x): 
    temp = {}
    for i in x:
        if i not in temp: 
            temp[i] = 1
        else:
            temp[i] += 1
    return temp

def make_anagram(a, b): 
    a1 = build_dict(a)
    b1 = build_dict(b)
    sum = 0
    for key in a1.keys():
        if key in b1.keys():
            sum += max(0, a1[key] - b1[key])
        else:
            sum += a1[key]
    for key in b1.keys(): 
        if key in a1.keys():
            sum += max(0, b1[key] - a1[key]) 
        else:
            sum += b1[key] 
    return sum

a = "markaaa"
b = "kram"

print(make_anagram(a, b))
# 3
```

**Use `Counter` function:**

```python
from collections import Counter

def make_anagram(a, b): 
    a1 = dict(Counter(a))
    b1 = dict(Counter(b))
    sum = 0
    for key in a1.keys():
        if key in b1.keys():
            sum += max(0, a1[key] - b1[key])
        else:
            sum += a1[key]
    for key in b1.keys(): 
        if key in a1.keys():
            sum += max(0, b1[key] - a1[key]) 
        else:
            sum += b1[key] 
    return sum
```

### Find anagrams

The function takes a `set` of words and returns groups of anagrams for those words. Each group must contain at least two words.
For example, if the input is "debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money", then there are three groups of anagrams:
(1) "debitcard", "badcredit"; (2)"elvis", "lives", "levis" (3)"silent", "listen"
Note that "money" does not appear in any group since it has no anagram in the set.

```python
import collections
def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list) 
    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends the original 
        # string as another value into hash table 
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)
    return [
        group for group in sorted_string_to_anagrams.values() if len(group) >= 2
    ]

dictionary = (
    "debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money" 
    )
groups = find_anagrams(dictionary) 
print(groups)
# [['debitcard', 'badcredit'], ['elvis', 'lives', 'levis'], ['silent', 'listen']]
```



### Interconvert strings and integers

```python
import functools
import string

def int_to_string(x): 
    is_negative = False 
    if x < 0:
        x, is_negative = -x, True

    s = [] 
    while True:
        s.append(chr(ord('0') + x % 10)) 
        x //= 10
        if x == 0:
            break
    # add the negative sing back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))

def string_to_int(s): 
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c), 
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

# Here, remember, True == 1 and False == 0, so s[True:] == s[1:], s[False:] == s[0:]
x = -123456
print(int_to_string(x))

x = "-7890"
print(string_to_int(x))
```

### Base conversion

Base conversion, from base b1 to base b2

```python
import string
import functools
def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else 
                construct_from_base(num_as_int // base, base) + 
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-' 
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0 )
    
    return (('-' if is_negative else '') + 
        ('0' if num_as_int == 0 else construct_from_base(num_as_int, b2)))

print(convert_base("FFFF", 16, 10 ))
# 65535
```

The time complexity is *O(n(1 + logb2 b1)*), where `n` is the length of `s`. The reasoning is as follows. First, we perform `n` multiply-and-adds to get `x` from `s`. Then we perform `Logb2 x` multiply and adds to get the result. The value `x` is upper-bounded by `b1**n, and logb2(b1**n) = n logb2 b1`.

