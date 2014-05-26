from task2 \
import task2_test_pyd

tests = task2_test_pyd.predefined_tests

def myFilter(L, num):
    return [x for x in L if x % num != 0]

exercise1 = myFilter

## Problem 2
def myLists(L):
    return [[y for y in range(1,x+1)] for x in L]
#print(myLists([1,2,4]))

exercise2 = myLists

## Problem 3
def myFunctionComposition(f, g):
    return {a:g[f[a]] for a in f}
#print (myFunctionComposition({0:'a', 1:'b'},{'a':'apple', 'b':'banana'}))
exercise3 = myFunctionComposition
## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5+3j
complex_addition_b = 1j
complex_addition_c = -1+0.001j
complex_addition_d = .001+9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    s = 0
    for l in L:
        try:
            s += l
        except:
            pass
    return s

exercise6 = mySum

## Problem 7
def myProduct(L):
    p = 1
    for l in L:
        try:
            p *= l
        except:
            pass
    return p

exercise7 = myProduct

## Problem 8
def myMin(L):
    if len(L) == 0: return None
    min = L[0]
    for l in L:
        if l < min: min = l
    return min

exercise8 = myMin

## Problem 9
def myConcat(L):
    s = ""
    for l in L:
        s += l
    return s

exercise9 = myConcat

## Problem 10
def myUnion(L):
    s = set()
    for l in L:
        s = s.union(l)
    return s

exercise10 = myUnion
#print (myUnion([{1},{},{2,1,1}]))