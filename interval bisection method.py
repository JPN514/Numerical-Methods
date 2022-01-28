#program for interval bisection root approximation method

import sympy as sym
import numpy as np

x = sym.Symbol('x')  #sets x as a symbol 

def getFunc():
    #get values from user as a list 
    f = sym.sympify(input("Enter function: ")) 
    interval = list(map(float,input("Enter a,b seperated by a comma: ").split(",")))
    tol = float(input("Enter error tolerance: "))
    Nmax = int(input("Enter the maximum  number of iterations: "))
    return f,interval,tol,Nmax

def method(f,interval,tol,Nmax):
    a = interval[0] #take the endpoints of the interval
    b = interval[1]
    i = 0 #counter

    #loop to track number of iterations up to given maximum
    while(i<Nmax):
        c = (a+b)/2  #calculate the midpoint of (a,b)
        #calculate the values of the function at points a,b,c for each iteration
        fa = f.subs(x,a)
        fb = f.subs(x,b)
        fc = f.subs(x,c)
        print("Step {}, a={}, b={}, c={}".format(i+1,a,b,c))
        print("f(a)={}, f(b)={}, f(c)={}".format(fa,fb,fc))
        if abs(fc) < tol:   #can end if the value f(c) is within the given error tolerance
            return c
        else: 
            if (fa > 0 and fc > 0) or (fa < 0 and fc < 0):   #can reassign the interval endpoints accordingly
                a = c
            else: 
                b = c        
        i += 1
    print("Maximum iterations reached.")
    return c

        



inputlist = getFunc()
print("f(x) = {}, [a,b] = {}, error tolerance = {}, maximum steps: {}.".format(*inputlist))

result = method(*inputlist) 
print("Estimate for root: {}".format(result))        # the * unpacks the list
