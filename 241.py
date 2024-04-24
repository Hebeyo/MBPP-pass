'''Write a function to generate a 3d array having each element as '*'.
'''
def array_3d(m,n,o):
    array_3d = []
    for i in range(o):
        array_3d.append([])
        for j in range(n):
            array_3d[i].append([])
            for k in range(m):
                array_3d[i][j].append('*')
    return array_3d
'''
Standard answer: 
def array_3d(m,n,o):
 array_3d = [[ ['*' for col in range(m)] for col in range(n)] for row in range(o)]
 return array_3d
'''
assert array_3d(6,4,3)==[[['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']]]
assert array_3d(5,3,4)==[[['*', '*', '*', '*', '*'], ['*', '*', '*', '*','*'], ['*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*'],['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]]
assert array_3d(1,2,3)==[[['*'],['*']],[['*'],['*']],[['*'],['*']]]
