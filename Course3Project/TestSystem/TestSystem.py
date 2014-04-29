import exercise_one as ex1
import io
import ast
import re
import inspect

predefined_vars = ['e1','e2','e3','e4','e5','e6','e7','e8']


testvars = vars(ex1).copy()
module_lines = list(open('exercise_one.py'))

def find_lines(lines, pattern=''):
    strings = list(filter(lambda l: pattern in l,lines))
    return strings

def find_line(lines, pattern=''):
    elem = list(filter(lambda l:pattern in l,lines))
    return elem[0] if len(elem) else None

def print_dumps(lines):
    for l in lines:
        print_dump(l)

def print_dump(line):
    dump = ast.dump(ast.parse(line))
    print("line: %sdump: %s\n" % (line,dump))

def isFunction(obj):
    return hasattr(obj, '__call__')

def verify_function(args, func1, func2):
    equivalent = True
    for arg in args:
        result1 = func1(arg)
        result2 = func2(arg)
        equivalent = equivalent and result1 == result2
        if not equivalent: return equivalent
    return equivalent
a = 0

def test_variables(variables):
    for v in predefined_vars:
        print(variables[v])
        a = variables[v]
        print(type(a))
    for x in [1,2,3]:
        print(variables['e7'](x))

def run_tests(tests={}):
    variables = sorted(tests.keys())
    for v in variables:
        print('tests for variable %s:' % v)
        good_job = True
        testvar = testvars[v]
        for test in tests[v]:            
            testfuncargs = test[0]
            testfunc = test[1]
            
            if(testfunc != None and len(testfuncargs)):
                if(isFunction(testvar)):
                    good_job = good_job and verify_function(testfuncargs,testvar,testfunc)
                elif testfunc.__name__ == 'find_line':
                    for funcarg in testfuncargs:
                        print('%s(\'%s\')\t\t' % (testfunc.__name__,funcarg))
                        good_job = good_job and testfunc(find_lines(module_lines,v),funcarg) != None
                elif len(inspect.getfullargspec(testfunc)[0]) == 2:
                    for funcarg in testfuncargs:
                        good_job = good_job and testfunc(funcarg,testvar)
                else:
                    good_job = good_job and testfunc(testvar)
                
        print('All tests completed successfully.' if good_job else 'Try next time, please. Fix errors.')
                        
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
    {'e1':[(['%','/'],find_line), ([0],e1_testfunction)],
     'e2':[(['ingstr','ing','ingstr'],find_line)],
     'e3':[([[1,2,3,4,5]],e3_testfunction)],
     'e4':[([],None)],
     'e5':[([0],e5_testfunction), (['e1','e2'],find_line)],
     'e6':[(['math','log'],find_line)],
     'e7':[([1,2,3,4],e7_testfunction)],
     'e8':[([],None)]
     }

run_tests(predefined_tests)