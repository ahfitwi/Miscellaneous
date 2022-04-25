
# Alem Fitwi

from pipe import *

#-----------------------------------------------------------------------
# A Decorator That Docorates Methods and Garners Their Names.
#-----------------------------------------------------------------------
def method(method):
    def dec(func):
        func.method = method
        return func
    return dec

#-----------------------------------------------------------------------
# Commonest Piping Methods
#-----------------------------------------------------------------------
class Piping:

    #------------------------------------------------------------------
    # Summing filtered values
    #------------------------------------------------------------------
    @method('sum_filtered')
    def sum_filtered():
        s1 = sum(range(100) | select(
            lambda x: x ** 2) | where(lambda x: x < 100))
        s2 = sum(range(100) | select(
            lambda x: x ** 2) | where(lambda x: x < 100))
        s3 = sum([1, 2, 3, 4] | where(lambda x: x % 2 == 0))
        s4 = sum([1, [2, 3], 4] | traverse)
        return s1+s2+s3+s4

    #------------------------------------------------------------------
    # tee
    #------------------------------------------------------------------
    @method('tee')
    def pipe_tee():
        return sum([1, 2, 3, 4, 5] | tee)

    #------------------------------------------------------------------
    # chain
    #------------------------------------------------------------------
    @method('pipe_chain')
    def pipe_chain():
        return list([[1, 2], [3, 4], [5]] | chain)

    #------------------------------------------------------------------
    # traverse
    #------------------------------------------------------------------
    @method('pipe_traverse')
    def pipe_traverse():
        return list([[1, 2], [[[3], [[4]]], [5]]] | traverse)
    #------------------------------------------------------------------
    # map
    #------------------------------------------------------------------
    @method('pipe_map')
    def pipe_map():
        return list([1, 2, 3] | map(lambda x: x * x))

    #------------------------------------------------------------------
    # select
    #------------------------------------------------------------------
    @method('pipe_select')
    def pipe_select():
        return list([1, 2, 3] | select(lambda x: x * x))

    #------------------------------------------------------------------
    # where
    #------------------------------------------------------------------
    @method('pipe_where')
    def pipe_where():
        return list([1, 2, 3] | where(lambda x: x % 2 == 0))

    #------------------------------------------------------------------
    # take_while
    #------------------------------------------------------------------
    @method('pipe_take_while')
    def pipe_take_while():
        return list([1, 2, 3, 4] | take_while(lambda x: x < 3))
    
    #------------------------------------------------------------------
    # skip_while
    #------------------------------------------------------------------
    @method('pipe_skip_while')
    def pipe_skip_while():
        return list([1, 2, 3, 4] | skip_while(lambda x: x < 3))

    #------------------------------------------------------------------
    # chain_with
    #------------------------------------------------------------------
    @method('pipe_chain_with')
    def pipe_chain_with():
        return list((1, 2, 3) | chain_with([4, 5], [6]))

    #------------------------------------------------------------------
    # take
    #------------------------------------------------------------------
    @method('pipe_take')
    def pipe_take():
        return list((1, 2, 3, 4, 5) | take(2))
   
    #------------------------------------------------------------------
    # tail
    #------------------------------------------------------------------
    @method('pipe_tail')
    def pipe_tail():
        return list((1, 2, 3, 4, 5) | tail(3))

    #------------------------------------------------------------------
    # skip
    #------------------------------------------------------------------
    @method('pipe_skip')
    def pipe_skip():
        return list((1, 2, 3, 4, 5) | skip(2))
    

    #------------------------------------------------------------------
    # islice()
    #------------------------------------------------------------------
    @method('pipe_islice')
    def pipe_islice():
        return list((1, 2, 3, 4, 5, 6, 7, 8, 9) | islice(2, 8, 2))

    #------------------------------------------------------------------
    # izip()
    #------------------------------------------------------------------
    @method('pipe_izip')
    def pipe_izip():
        return list((1, 2, 3, 4, 5, 6, 7, 8, 9)| izip(
            [9, 8, 7, 6, 5, 4, 3, 2, 1]))

    #------------------------------------------------------------------
    # groupby()
    #------------------------------------------------------------------
    @method('pipe_groupby')
    def pipe_groupby():
        return (1, 2, 3, 4, 5, 6, 7, 8, 9) \
            | groupby(lambda x: x % 2 and "Even" or "Odd")\
            | select(lambda x: "%s : %s" % (x[0], (x[1] | concat(', '))))\
            | concat(' / ')

    #------------------------------------------------------------------
    # sort()
    #------------------------------------------------------------------
    @method('pipe_sort')
    def pipe_sort():
        lst1 = list([5, -4, 3, -2, 1] | sort(key=abs))
        lst2 = ''.join("python" | sort)
        return lst1, lst2 

    #------------------------------------------------------------------
    # dedup()
    #------------------------------------------------------------------
    @method('pipe_dedup')
    def pipe_dedup():
        lst1 = list([1, 1, 2, 2, 3, 3, 1, 2, 3] | dedup)
        lst2 = list([1, 1, 2, 2, 3, 3, 1, 2, 3] | dedup(key=lambda n:n % 2))
        return lst1, lst2

    #------------------------------------------------------------------
    # uniq()
    #------------------------------------------------------------------
    @method('pipe_uniq')
    def pipe_uniq():
        lst1 = list([1, 1, 2, 2, 3, 3, 1, 2, 3] | uniq)
        lst2 = list([1, 1, 2, 2, 3, 3, 1, 2, 3] | uniq(key=lambda n:n % 2))
        return lst1, lst2

    #------------------------------------------------------------------
    # reverse
    #------------------------------------------------------------------
    @method('pipe_reverse')
    def pipe_reverse():
        return list([1, 2, 3] | reverse)

    #------------------------------------------------------------------
    # strip
    #------------------------------------------------------------------
    @method('pipe_strip')
    def pipe_strip():
        lst1 = '  abc   ' | strip
        lst2 = '.,[abc] ] ' | strip('.,[] ')
        return lst1, lst2

    #------------------------------------------------------------------
    # rstrip
    #------------------------------------------------------------------
    @method('pipe_rstrip')
    def pipe_rstrip():
        lst1 = '  abc   ' | rstrip
        lst2 = '.,[abc] ] ' | rstrip('.,[] ')
        return lst1, lst2

    #------------------------------------------------------------------
    # lstrip
    #------------------------------------------------------------------
    @method('pipe_strip')
    def pipe_lstrip():
        lst1 = '  abc   ' | lstrip
        lst2 = '.,[abc] ] ' | lstrip('.,[] ')
        return lst1, lst2

    #------------------------------------------------------------------
    # permutations
    #------------------------------------------------------------------
    @method('pipe_permutations')
    def pipe_permutations():
        lst1 = list('ABC' | permutations(2))
        lst2 = list(range(3) | permutations)
        return lst1, lst2


    #------------------------------------------------------------------
    # transpose
    #------------------------------------------------------------------
    @method('pipe_transpose')
    def pipe_transpose():
        return [[1, 2, 3], [4, 5, 6], [7, 8, 9]] | transpose
    
    
#-----------------------------------------------------------------------
#  To Dictionary: (func_name, func_call)
#-----------------------------------------------------------------------
def todct(Class):
    method_lst = {}
    for name, attrib in vars(Class).items():
        if callable(attrib):
            method = attrib.method
            if method not in method_lst:
                method_lst[method]=[]
            method_lst[method].append(attrib)
    return method_lst

#-----------------------------------------------------------------------
#  Execute Methods one by one
#-----------------------------------------------------------------------

def execute_func(function, *args):
    return function(*args)

#-----------------------------------------------------------------------
#  Main()
#-----------------------------------------------------------------------

methods = todct(Piping)
for m in methods:
    print(m)

"""
Results:
(base) alem@alem-Legion-S7-15ACH6:~/Desktop$ python piping.py
sum_filtered
tee
pipe_chain
pipe_traverse
pipe_map
pipe_select
pipe_where
pipe_take_while
pipe_skip_while
pipe_chain_with
pipe_take
pipe_tail
pipe_skip
pipe_islice
pipe_izip
pipe_groupby
pipe_sort
pipe_dedup
pipe_uniq
pipe_reverse
pipe_strip
pipe_rstrip
pipe_permutations
pipe_transpose
"""
print("-------------------------------------------------------")
for m in methods.keys():
    print(f"{m}: {execute_func(methods[m][0])}")

"""
-------------------------------------------------------
sum_filtered: 586
1
2
3
4
5
tee: 15
pipe_chain: [1, 2, 3, 4, 5]
pipe_traverse: [1, 2, 3, 4, 5]
pipe_map: [1, 4, 9]
pipe_select: [1, 4, 9]
pipe_where: [2]
pipe_take_while: [1, 2]
pipe_skip_while: [3, 4]
pipe_chain_with: [1, 2, 3, 4, 5, 6]
pipe_take: [1, 2]
pipe_tail: [3, 4, 5]
pipe_skip: [3, 4, 5]
pipe_islice: [3, 5, 7]
pipe_izip: [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)]
piping.py:139: DeprecationWarning: pipe.concat is deprecated, use ', '.join(your | pipe) instead.
  | concat(' / ')
piping.py:138: DeprecationWarning: pipe.concat is deprecated, use ', '.join(your | pipe) instead.
  | select(lambda x: "%s : %s" % (x[0], (x[1] | concat(', '))))\
pipe_groupby: Even : 1, 3, 5, 7, 9 / Odd : 2, 4, 6, 8
pipe_sort: ([1, -2, 3, -4, 5], 'hnopty')
pipe_dedup: ([1, 2, 3], [1, 2])
pipe_uniq: ([1, 2, 3, 1, 2, 3], [1, 2, 3, 2, 3])
pipe_reverse: [3, 2, 1]
pipe_strip: ('abc', 'abc')
pipe_rstrip: ('  abc', '.,[abc')
pipe_permutations: ([('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')], [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)])
pipe_transpose: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
(base) alem@alem-Legion-S7-15ACH6:~/Desktop$ 
"""
#-----------------------------------------------------------------------
#                               ~END~
#-----------------------------------------------------------------------