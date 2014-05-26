def find_line(lines, pattern=''):
    elem = list(filter(lambda l:pattern in l,lines))
    return elem[0] if len(elem) else None
###
#START>>>Section for predefined test functions
###
def __e1_testfunction__(obj):
    return obj > 10

def __e3_testfunction__(o1,o2):
    return True if o1 == o2 else None

def __e5_testfunction__(o1):
    return type(o1) is tuple

def __e7_testfunction__(a):
    return a * a
###
#END>>>Section for predefined test functions
###

def __PyInit_pyd__():
    import task1 as t1
    return t1

predefined_tests = \
    {'exercise1':[(['%','/'],find_line), ([0],__e1_testfunction__)],
     'exercise2':[(['ingstr','ing','ingstr'],find_line)],
     'exercise3':[([[1,2,3,4,5]],__e3_testfunction__)],
     'exercise4':[([],None)],
     'exercise5':[([[0]],__e5_testfunction__), (['exercise1','exercise2'],find_line)],
     'exercise6':[(['math','log'],find_line)],
     'exercise7':[([[1],[2],[3],[4]],__e7_testfunction__)],
     'exercise8':[([],None)]
     }