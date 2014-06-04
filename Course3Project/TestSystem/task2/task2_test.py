from common_tools import tools

def find_line(lines, pattern=''):
    elem = list(filter(lambda l:pattern in l,lines))
    return elem[0] if len(elem) else None
###
#START>>>Section for predefined test functions
###

## Problem 1
def myFilter(L, num):
    return [x for x in L if x % num != 0]


## Problem 2
def myLists(L):
    return [[y for y in range(1,x+1)] for x in L]
#print(myLists([1,2,4]))


## Problem 3
def myFunctionComposition(f, g):
    return {a:g[f[a]] for a in f}
#print (myFunctionComposition({0:'a', 1:'b'},{'a':'apple', 'b':'banana'}))

## Problem 4
# Please only enter your numerical solution.

def equality(a,b):
    return a == b

#5+3j, 1j, -1+0.001j, .001+9j



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



## Problem 7
def myProduct(L):
    p = 1
    for l in L:
        try:
            p *= l
        except:
            pass
    return p



## Problem 8
def myMin(L):
    if len(L) == 0: return None
    min = L[0]
    for l in L:
        if l < min: min = l
    return min



## Problem 9
def myConcat(L):
    s = ""
    for l in L:
        s += l
    return s


## Problem 10
def myUnion(L):
    s = set()
    for l in L:
        s = s.union(l)
    return s

###
#END>>>Section for predefined test functions
###5+3j, 1j, -1+0.001j, .001+9j

#predefined_tests = \
#    {'exercise1':[([[[1,2,3,4],4],[[70,80],4]],myFilter)],
#     'exercise2':[([[[1,0,0,0]]],myLists)],
#     'exercise3':[([],None)],
#     'complex_addition_a':[([5+3j],equality)],
#     'complex_addition_b':[([1j],equality)],
#     'complex_addition_c':[([-1+0.001j],equality)],
#     'complex_addition_d':[([.001+9j],equality)],
#     'GF2_sum_1':[([1],equality)],
#     'GF2_sum_2':[([0],equality)],
#     'GF2_sum_3':[([0],equality)],
#     'exercise6':[([],None)],
#     'exercise7':[([],None)],
#     'exercise8':[([],None)],
#     'exercise9':[([],None)],
#     'exercise10':[([],None)],
#     }

###  TESTS  ###

exercise1Test1 = tools.Test('my Filter test', myFilter, [ [[1,2,3,4],4], [[70,80],4] ])
exercise1Test1.answer.OK = 'Filtered data is correct'
exercise1Test1.answer.Fail = 'Filtered data is incorrect'

exercise2Test1 = tools.Test('my List test', myLists, [ [[1,0,0,0]] ])
exercise2Test1.answer.OK = 'List data is correct'
exercise2Test1.answer.Fail = 'List data is incorrect'

complex_addition_aTest1 = tools.Test('equality', equality, [5+3j])

complex_addition_bTest1 = tools.Test('equality', equality, [1j])

complex_addition_cTest1 = tools.Test('equality', equality, [-1+0.001j])
complex_addition_cTest2 = tools.Test('Find line test', find_line, ['+','-','j'])

complex_addition_dTest1 = tools.Test('equality', equality, [.001+9j])

predefined_tests = \
    {'exercise1':[exercise1Test1],
     'exercise2':[exercise2Test1],
     'exercise3':[tools.Test()],
     'complex_addition_a':[complex_addition_aTest1],
     'complex_addition_b':[complex_addition_bTest1],
     'complex_addition_c':[complex_addition_cTest1, complex_addition_cTest2],
     'complex_addition_d':[complex_addition_dTest1],
     'GF2_sum_1':[tools.Test('equality', equality, [1])],
     'GF2_sum_2':[tools.Test('equality', equality, [0])],
     'GF2_sum_3':[tools.Test('equality', equality, [0])],
     'exercise6':[tools.Test()],
     'exercise7':[tools.Test()],
     'exercise8':[tools.Test()],
     'exercise9':[tools.Test()],
     'exercise10':[tools.Test()],
     }