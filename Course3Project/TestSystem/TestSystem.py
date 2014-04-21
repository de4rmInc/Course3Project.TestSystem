import exercise_one as ex1
import io
import ast
import re

predefined_vars = ['e1','e2','e3','e4','e5','e6']


testvars = vars(ex1).copy()
module_lines = list(open('exercise_one.py'))

def find_lines(lines,pattern=''):
    strings = list(filter(lambda l: pattern in l,lines))
    return strings

def find_line(lines,pattern=''):
    elem = list(filter(lambda l:pattern in l,lines))
    return elem[0] if len(elem) else None

def print_dumps(lines):
    for l in lines:
        print_dump(l)

def print_dump(line):
    dump = ast.dump(ast.parse(line))
    print("line: %sdump: %s\n" % (line,dump))

a = 0

def test_variables(variables):
    for v in predefined_vars:
        print(variables[v])
        a = variables[v]
        print(type(a))
    for x in [1,2,3]:
        print(variables['e7'](x))

def run_tests(tests={},variables=[]):
    for v in variables:
        testfuncvars= predefined_tests[v][0]
        testfunc = predefined_tests[v][1]

        print('tests for variable %s:'%v)

        if(testfunc != None and len(testfuncvars)):
            for funcvar in testfuncvars:
                print('%s(\'%s\')\t\t'%(testfunc.__name__,funcvar))
                print(testfunc(find_lines(module_lines,v),funcvar) != None)

test_variables(testvars)
print(find_lines(module_lines))

print_dumps(find_lines(module_lines))



predefined_tests = \
    {'e1':(['%'],find_line),
     'e2':(['str','ing','ingstr'],find_line),
     'e3':([],None),
     'e4':([],None),
     'e5':([],None),
     'e6':([],None)}

run_tests(predefined_tests,predefined_vars)

#testvars_temp = [x for x in predefined_tests['e1'][0]]
#testfunc = predefined_tests['e1'][1]

#if(testfunc != None and len(testvars_temp)):
#    print(testfunc(find_lines(module_lines,'e1'),testvars_temp[0]) != None)