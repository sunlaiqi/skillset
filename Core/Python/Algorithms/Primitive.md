- [Primitive Types](#primitive-types)
  - [Bitwise operator](#bitwise-operator)
    - [x & 1](#x--1)
    - [Computing the parity of a word](#computing-the-parity-of-a-word)
    - [Swap BITS](#swap-bits)
    - [Reverse Bits??](#reverse-bits)
    - [Find a closest integer with the same weight](#find-a-closest-integer-with-the-same-weight)
    - [Set and flip a bit:](#set-and-flip-a-bit)
  - [Top tips for primitive types](#top-tips-for-primitive-types)
  - [random](#random)
    - [How to shuffle a list (array): (suppose a is a list)](#how-to-shuffle-a-list-array-suppose-a-is-a-list)


# Primitive Types

## Bitwise operator

Operator    |Name            |Description
------------|----------------|---------------------------------------
`&`           |AND             |Sets each bit to 1 if both bits are 1
&#124;          |OR              |Sets each bit to 1 if one of two bits is 1
`^`           |XOR (circumflex)|Sets each bit to 1 if only one of two bits is 1
`~`           |NOT (tilde)            |Inverts all the bits (~n = -n -1)
`<<`          |Zero fill left shift   |Shift left by pushing zeros in from the right and let the leftmost bits fall off
`>>`          |Signed right shift     |Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

### x & 1 

x & 1 = 1 if the last bit of x is 1, 0 if the last bit is 0

Count the number of bits that are set to 1 in a positive integer

```python
def count_bits(x): 
    num_bits = 0 
    while x:
        num_bits += x & 1
        x >>= 1 
    return num_bits
```
The time complexity is *O(n)*.
```python
sys.maxsize == 2^63 -1
6&4 == 4 
1|2 == 3
8 >> 2 == 2
-16 >> 2 == -4
1 << 10 == 1024
~0 == -1
~n == (-n -)
15^1 == 14
15^2 == 13
15^3== 12
15^x == 15 - x # (x <=15) 
16^1 == 17
16^2 == 18
16^3 == 19
16^x = 16 + x # (x < 16) 
16^16 == 0
15^15 == 0
15^16 == 31
15^17 == 30
15^18 = 29

```

### Computing the parity of a word

The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.

1. Brute force:

```python
def parity(x): 
    result = 0
    while x:
        result ^= x & 1 
        x >>= 1
    return result
```
The time complexity is *O(n)*, where n is the word size.

2. x & (x - 1) equals x with its lowest set bit erased

```python
def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # Drops the -lowest set bit of x 
    return result
```
`x & (x - 1)` equals `x` with its lowest set bit erased. This fact can be used to reduce the time complexity. Let `k` be the number of bits set to 1 in a particular word. (For example, for 10001010, k = 3.) Then time complexity of the algorithm below is *O(k)*.

`x & ~(x - 1)` isolates the lowest bit that is 1 in `x`:
```python
3 & ~(3-1) == 1 
12 & ~(12-1) == 4
```

`(x & 1)`: judge if the last bit of `x` is 1, return 1 only when the last is 1

3. Use XOR
The order we perform the XORs does not change the result. The XOR of a group of bits is its parity. For example, the parity of (b63,b62,. .. ,b3,b2, b1, b0) equals the parity of the `XOR of (b63b62,. . . ,b32) and (b31, b30,. .., b0)`. We repeat the same operation on 32-,16-,8-, 4-, 2-, and 1-bit operands to get the final result. 
Note that the leading bits are not meaningful, and we have to explicitly extract the result from the **least-significant bit**.

The last bit is the result, and to extract it we have to bitwise-AND with (00000001).

```python
def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1 
    return x & 0x1
```
The time complexity is *O(log n)*, where n is the word size.

### Swap BITS
Firstly, we test if the bits to be swapped differ. If they do not, the swap does not change the integer. 
If the bits are different, swapping them is the same as flipping their individual values.
```python
def swap_bits(x, i, j):
    # Extract the i-th and j-th bits, and see if they differ. 
    if (x >> i) & 1 != (x >> j) & 1:
    # i-th and j-th bits differ. We will swap them by flipping their values. 
    # Select the bits to flip with bit_mask. Since x^1 = 0 when x = 1 and 
    # 1 when x = 0, we can perform the flip XOR.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask 
    return x
```
The time complexity is *O(1)*, independent of the word size.

### Reverse Bits??

Write a program that takes a 64-bit unsigned integer and returns the 64-bit unsigned integer consisting of the bits of the input in reverse order.
We illustrate the approach with 8-bit integers and 2-bit lookup table keys. The table is rev = ((00),(10),(01),(11)). If the input is (10010011), its reverse is rev(11),rev(00),rev(01),rev(10), i.e., (11001001).
```python
def reverse_bits(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE) | PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE) | PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE | PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) & BIT_MASK])
```
The time complexity is O(n/L) for n-bit integers and L-bit cache keys.


Use `swap_bits()` function??

### Find a closest integer with the same weight
Define the weight of a nonnegative integer x to be the **number of bits that are set to 1** in its binary representation. For example, since 92 in base-2 equals (1011100), the weight of 92 is 4.

Problem:
Write a program which takes as input a nonnegative integer x and returns a number y which is not equal to x, but has the **same weight** as x and their difference, `|y - x|`, is as small as possible.

Solution:
Suppose we flip the bit at index `k1` and flip the bit at index `k2`, `k1 > k2`. Then the absolute value of the difference between the original integer and the new one is `(2**k1 - 2**k2)`. To minimize this, we should make `k1` as small as possible and `k1` as close to `k2`.
In summary, the correct approach is to swap the two **rightmost consecutive** bits that differ.

```python
def closest_int_same_bit_count(x): 
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1)) # Swaps bit-i and bit-(i+1) 
            return x
    # raise error if all bits of x are 0 or 1
    raise ValueError(‘All bits are 0 or 1’)
```
The time complexity is *O(n)*, where `n` is the integer width. 

**Variant: solve the same problem in O(1) time and space.**

**Solution:**
Utilize `x & ~(x - 1)` isolates the lowest bit that is 1 in `x`.
`x ^ (x + 1)` isolates the lowest bit 0 but set 1

```python
def closest_int_same_bit_count(x):
    # Obtain the lowest bit 1
    if x == 0 or (x + 1) & x == 0:
        raise ValueError('All bits are 0 or 1')

    y = x & ~(x - 1)
    # Get the number of bits of y 
    l = len(bin(y)[2:]) - 1     # remove first two characters 0b.
    if l > 0:
        x ^= (1 << l) | (1 << (l - 1))  # Swaps bit-l and bit-(l-1) 
        return x
    else:
        # What to do if the 1st bit is 1?
        z = x ^ (x + 1) # Isolate the lowest bit 0 but set 1
        lz = len(bin(z)[2:]) - 1
        x ^= (1 << lz) | (1 << (lz - 1))  # Swaps bit-lz and bit-(lz-1) 
        return x

print(closest_int_same_bit_count(9))    # == 10
print(closest_int_same_bit_count(8))    # == 4
```

### Set and flip a bit:

**How to set a bit:**
Create a bit mask based on the position passed in. It produces '10000' if we pass in position=4 our bit in the '4th' position is set to 1 
```python

def set_bit(position, binary):
    bit_mask = 1 << position
    # return our binary string or-ed with our mask 
    return bit_mask | binary

# This should return 16
print(set_bit(4, 00000000))
```

**How to flip a bit**:
```python
def flip_bit(position, binary):
    bit_mask = 1 << position
    return binary ^ bit_mask
```

**MSB vs LSB**
Most Significant Bit vs Least Significant Bit



## Top tips for primitive types


XOR - Exclusive OR: The resulting bit evaluates to one if only exactly one of the bits is set.

Know fast ways to *clear the lowermost set bit* (and by extension, set the lowermost 0, get its index, etc.) 
`(x & (x-1))`

Consider using a `cache` to accelerate operations by using it to brute-force small inputs.
For example, use a global variable to store temp summary for a for-in loop.

Be aware that commutativity and associativity can be used to perform operations in parallel and reorder operations.

Unlike integers, floats are not infinite precision, and it's convenient to refer to infinity as float('inf') and float('-inf '). These values are comparable to integers, and can be used to create psuedo max-int and pseudo min-int.
```python
positive_infnity = float('inf')
negative_infnity = float('-inf')

import math 
  
# Defining a positive infinite integer 
positive_infnity = math.inf 
  
# Defining a negative infinite integer 
negative_infinity = -math.inf 

>>> math.inf == float('inf')
True

```

## random

The key methods in random are:
- random.randrange(28)
- random.randint(8,16)
- random.random()
- random.shuffle(A)
- random.choice(A).
```python
>>> Random.randrange(28, 28), 
ValueError: empty range for randrange() (28,28, 0)
>>> random.randint(16,16) == 16
True
>>> Random.random()
0.3947786420485154
>>> random.choice('abcdefg')
'e'
```

### How to shuffle a list (array): (suppose a is a list)
```python
import random
a = [a[x] for x in random.sample(range(len(a)), len(a))]
# Or just use 
random.shuffle(a)
```

