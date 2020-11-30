- [Sorting](#sorting)
  - [Quick sorting](#quick-sorting)
    - [Principle](#principle)
    - [Quicksort in quick review](#quicksort-in-quick-review)
    - [Three implementation of sort](#three-implementation-of-sort)
  - [Selection sort](#selection-sort)
  - [Bubble Sort](#bubble-sort)


# Sorting

## Quick sorting

### Principle

Empty arrays and arrays with just one element will be the base case. You can just return those arrays as is — there’s nothing to sort:

```python
def quicksort(array): 
    if len(array) < 2:
        return array
```

Remember, you are using **Divide & Conquer**. So you want to break down this array until you are at the base case.

Here is how Quicksort works. 
- First, pick up an element from the array. This element is called **pivot**. Let’s say, the first element in the array is the pivot.
- Now find the elements smaller than the pivot and the elements larger than the pivot. This is called **partitioning**. Now you have
    - A sub-array of all the numbers less than the pivot
    - The pivot
    - A sub-array of all the numbers greater than the pivot
- If the sub-arrays are sorted, then you can combine the whole things like this (recursive):
  - left array + pivot + right array
- And you get a sorted array.

### Quicksort in quick review

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

### Three implementation of sort

quicksort(best), quick_sort, select_sort(brute force, worst)

```python
import time
z = [38,3,6,4,9,10,30,2,5,7,9,21,12,43,9,1,6,56,89,23,34,5,3,6,4,9,10,30]

def quick_sort(x): 
    if len(x) < 2:
        return x 
    else:
        pivot = x[0]
        left_list = []
        right_list = []
        
        for i in range(1, len(x)):
            time.sleep(0.01) 
            print("#", end="")
            if x[i] <= pivot:
                left_list.append(x[i])
            else: 
                right_list.append(x[i])
        
        return quick_sort(left_list) + [pivot] + quick_sort(right_list)

def quicksort(array): 
    if len(array) < 2:
        return array 
    else:
        time.sleep(0.01)
        print("#", end="")
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    
    return quicksort(less) + [pivot] + quicksort(greater)

def select_sort(x):
    for i in range(len(x)):
        for j in range(i, len(x)): 
            time.sleep(0.01)
            print("#", end="")
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i] 
    return x
print(quicksort(z))
print(quick_sort(z))
print(select_sort(z))
```

The worst case time complexity of a typical implementation of QuickSort is *O(n**2)*. 
The worst case occurs when the picked pivot is always an extreme (smallest or largest) element. This happens when input array is **sorted** or reverse sorted and either first or last element is picked as pivot. Although **randomized QuickSort** works well even when the array is sorted, there is still possibility that the randomly picked element is always an extreme.

Can the worst case be reduced to *O(nLogn)*? The answer is yes, we can achieve *O(nLogn)* worst case. The idea is based on the fact that the **median element** of an unsorted array can be found in linear time. So we find the median first, then partition the array around the median element.


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





