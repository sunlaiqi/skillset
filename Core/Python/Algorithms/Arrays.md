


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