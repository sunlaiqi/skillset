

# cache, lru_cache

## Implementing a Cache Using a Python Dictionary

```python
import requests

cache = dict()

def get_article_from_server(url):
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text

def get_article(url):
    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)

    return cache[url]

get_article("https://realpython.com/sorting-algorithms-python/")
get_article("https://realpython.com/sorting-algorithms-python/")
```

## Caching Strategies
There’s one big problem with this cache implementation: the content of the dictionary will grow indefinitely! 
To work around this issue, you need a strategy to decide which articles should stay in memory and which should be removed. 

## Diving Into the Least Recently Used (LRU) Cache Strategy

Every time you access an entry, the LRU algorithm will move it to the top of the cache.

One way to implement an LRU cache in Python is to use a combination of a doubly linked list and a hash map. The `head` element of the doubly linked list would point to the most recently used entry, and the `tail` would point to the least recently used entry.

Using the hash map, you can ensure access to every item in the cache by mapping each entry to the specific location in the doubly linked list.

This strategy is very fast. Accessing the least recently used item and updating the cache are operations with a runtime of O(1).

## Using @lru_cache to Implement an LRU Cache in Python

Just like the caching solution you implemented earlier, @lru_cache uses a dictionary behind the scenes. It caches the function’s result under a key that consists of the call to the function, including the supplied arguments. This is important because it means that these arguments have to be **hashable** for the decorator to work.

Run following program will se huge performance difference between with @lru_cache and without @lru_cache.

```python
from timeit import repeat
from functools import lru_cache

@lru_cache
def steps_to(stair):
    if stair == 1:
        # You can reach the first stair with only a single step
        # from the floor.
        return 1
    elif stair == 2:
        # You can reach the second stair by jumping from the
        # floor with a single two-stair hop or by jumping a single
        # stair a couple of times.
        return 2
    elif stair == 3:
        # You can reach the third stair using four possible
        # combinations:
        # 1. Jumping all the way from the floor
        # 2. Jumping two stairs, then one
        # 3. Jumping one stair, then two
        # 4. Jumping one stair three times
        return 4
    else:
        # You can reach your current stair from three different places:
        # 1. From three stairs down
        # 2. From two stairs down
        # 2. From one stair down
        #
        # If you add up the number of ways of getting to those
        # those three positions, then you should have your solution.
        return (
            steps_to(stair - 3)
            + steps_to(stair - 2)
            + steps_to(stair - 1)
        )

setup_code = "from __main__ import steps_to"
stmt = "steps_to(30)"
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
print(f"Minimum execution time: {min(times)}")
```

## Unpacking the Functionality of @lru_cache

With the @lru_cache decorator in place, you store every call and answer in memory to access later if requested again. But how many calls can you save before running out of memory?

Python’s @lru_cache decorator offers a maxsize attribute that defines the maximum number of entries before the cache starts evicting old items. By default, maxsize is set to 128. If you set maxsize to None, then the cache will grow indefinitely, and no entries will be ever evicted. 

In this case, you’re limiting the cache to a maximum of 16 entries. When a new call comes in, the decorator’s implementation will evict the least recently used of the existing 16 entries to make a place for the new item.

To see what happens with this new addition to the code, you can use `cache_info()`, provided by the @lru_cache decorator, to inspect the number of hits and misses and the current size of the cache. 

```python
print(steps_to(30))
print(steps_to.cache_info())
```
```
53798080
CacheInfo(hits=52, misses=30, maxsize=16, currsize=16)
```