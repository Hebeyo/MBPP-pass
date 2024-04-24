'''Write a function for computing square roots using the babylonian method.
'''
def babylonian_squareroot(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
'''
Standard answer: 
def babylonian_squareroot(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
'''
assert babylonian_squareroot(10)==3.162277660168379
assert babylonian_squareroot(2)==1.414213562373095
assert babylonian_squareroot(9)==3.0
