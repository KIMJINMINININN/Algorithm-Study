# Algorithm-Study
### 백준 문제
#### Greedy
### 책(이것이 취업을 위한 코딩 테스트다 with 파이썬))

---------------------------------------

### collection
#### dic(Counter) -> dic
#### sum(list, []) -> ex)2차원을 1차원으로



### 재귀를 사용할때 메모리 효율적
```
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n:int)->int:
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print(fib(10))

// ans = 55
// 1 1 2 3 5 8 13 21 34 55 
```