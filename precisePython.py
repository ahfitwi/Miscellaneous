# 1. Negative indexing
a = [1,2,3]
print(f"a[-2]: {a[-2]}") 
print(f"a[-2]: {a[-1]}") 

# 2. List slices
a = [1,2,3,4]
print(f"a[2:4]: {a[2:4]}") 

# 3. Grouped naming
a,b,c = [1,2,3]

# 4. Set operations
a = {1,2,3,6,2,3}
b = {4,2,5,7,4,3}
print(f"a | b: {a|b}") 
print(f"a & b: {a&b}")
print(f"a - b: {a-b}")
print(f"a ^ b: {a^b}")

# 5. nLargest and nSmallest
import heapq 
a = [3,2,5,6,7,34,8,3,42,4,5] 
print(f"5smallest: {heapq.nsmallest(5,a)}")
print(f"3largest: {heapq.nlargest(3,a)}") 

# 6. Cartesian products
import itertools 
[print(p) for p in itertools.product([4,3,6,2],[3,6])]

# 7. Inverting a dictionary
a = {'a':1,'b':2,'c':3} 
dct = {x: y for y, x in a.items()}
print(f"inverted dct: {dct}") 

# 8. Generators
a = (x+1 for x in range(10)) 
next(a)  
next(a) 
next(a)

# 9. Named tuples
import collections 
Point = collections.namedtuple('Point',['x','y']) 
p = Point(x=1,y=3) 
print(f"p = {p}")

#10. Flatten lists
a = [[1,2],[4,3],[5,2, [4,5]]] 
print(f"flattened: {sum(a,[])}") 
