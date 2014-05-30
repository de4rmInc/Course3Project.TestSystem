from common_tools import tools

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

predefined_tests = \
    {'exercise1':[
                  tools.Test( find_line, ['%','/']),
                  tools.Test(__e1_testfunction__, [0])
                  ],
     'exercise2':[
                  tools.Test(find_line, ['ingstr','ing','ingstr'])
                  ],
     'exercise3':[
                  tools.Test(__e3_testfunction__, [[1,2,3,4,5]])
                  ],
     'exercise4':[tools.Test()],
     'exercise5':[
                  tools.Test(__e5_testfunction__,[[0]]),
                  tools.Test(find_line, ['exercise1','exercise2'])
                  ],
     'exercise6':[
                  tools.Test(find_line, ['math','log'])
                  ],
     'exercise7':[
                  tools.Test(__e7_testfunction__, [[1],[2],[3],[4]])
                  ],
     'exercise8':[tools.Test()]
     }