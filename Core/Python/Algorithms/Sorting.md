- [Sorting](#sorting)
  - [Quick sorting](#quick-sorting)
    - [Principle](#principle)
    - [Three implementation of sort](#three-implementation-of-sort)


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