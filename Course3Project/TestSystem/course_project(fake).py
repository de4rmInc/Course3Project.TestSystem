import exercise_one as ex1
import io,ast

predefined_vars=['e1','e2','e3','e4','e5','e6']

testvars=vars(ex1).copy()

def find_lines(module_path):
    f_strings=list(open(module_path))
    return f_strings

def print_dumps(lines):
    for l in lines:
        print_dump(l)

def print_dump(line):
    dump=ast.dump(ast.parse(line))
    print("line: %sdump: %s\n" % (line,dump))

a=0

def test_variables(variables):
    for v in predefined_vars:
        print(variables[v])
        a=variables[v]
        print(type(a))
    for x in [1,2,3]:
        print(variables['e7'](x))

test_variables(testvars)
print(find_lines('exercise_one.py'))

print_dumps(find_lines('exercise_one.py'))