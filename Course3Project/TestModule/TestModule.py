import TestModuleLib as tml

def start_tests():
    result = tml.start_tests()
    if(len(result)):
        for dir_name in result:
            print('== %s'%dir_name)
            for arg in result[dir_name]:
                print('\t== %s'%arg)
                for test in result[dir_name][arg]:
                    print('\t\t== %s'%result[dir_name][arg][test])

