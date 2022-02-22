

# PURE FUNCTION

# example 1
A = 7
def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b

impure_sum(6)                                           # returns 13     
pure_sum(3,4)                                           # returns 7


# example 2
def read(filename):
    with open (filename, 'r') as f:
        return [line for line in f]
    
def count (lines):
    return len(lines)

example_lines = read('deneme.txt')
lines_count = count(example_lines)
lines_count


# ANONYMOUS FUNCTION

def old_sum(a,b):
    return a + b
old_sum(4,5)

new_sum = lambda a,b : a+b
new_sum(5,6)                                            # returns 11

unorder_list = [('b',3),('a',8),('d',12),('c',1)]
sorted(unorder_list, key=lambda x : x[1])               # returns [('c', 1), ('b', 3), ('a', 8), ('d', 12)]




# VECTOR OPERATIONS

import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b                                                     # returns array([ 2,  6, 12, 20])



# MAP, FILTER, REDUCE FUNCTIONS

# map --->>> values change
listtt = [1,2,3,4,5]
list(map(lambda x: x + 10, listte))                     # returns [11, 12, 13, 14, 15]

#filter --->>> values don't change
listt = [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x %2 == 0, listt))                # returns [2, 4, 6, 8, 10]

#reduce
from functools import reduce
listtt = [1,2,3,4,5]
reduce(lambda a,b: a + b, listtt)                       # returns 15



