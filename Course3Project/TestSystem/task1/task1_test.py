def find_line(lines, pattern=''):
    elem = list(filter(lambda l:pattern in l,lines))
    return elem[0] if len(elem) else None
###
#START>>>Section for predefined test functions
###
def e1_testfunction(obj):
    return obj > 10

def e3_testfunction(o1,o2):
    return True if o1 == o2 else None

def e5_testfunction(o1):
    return type(o1) is tuple

def e7_testfunction(a):
    return a * a
###
#END>>>Section for predefined test functions
###

predefined_tests = \
    {'exercise1':[(['%','/'],find_line), ([0],e1_testfunction)],
     'exercise2':[(['ingstr','ing','ingstr'],find_line)],
     'exercise3':[([[1,2,3,4,5]],e3_testfunction)],
     'exercise4':[([],None)],
     'exercise5':[([0],e5_testfunction), (['exercise1','exercise2'],find_line)],
     'exercise6':[(['math','log'],find_line)],
     'exercise7':[([1,2,3,4],e7_testfunction)],
     'exercise8':[([],None)]
     }
