#Newton-Raphson method 
# for root approximations

import numpy as np
import sympy as sym

x = sym.Symbol('x')  #sets x as a symbol 
#print(sym.diff(x**5)) #diff gives derivative of the input
#f = sym.sympify(input("Enter function: ")) #takes user input and simplifys using sympy
#print(f)
#print(f.subs(x,5)) #subs to sub in a value for x



def getFunc():
    #get values from user as a list 
    f = sym.sympify(input("Enter function: "))
    fprime = sym.diff(f)
    x0 = float(input("Enter estimate for the root: "))
    tol = float(input("Enter error tolerance: "))
    return f,fprime,x0,tol


def method(f,fprime,x0,tol):
    #Newton-Raphson step to return root approx of f via recursion
    if(abs(f.subs(x,x0)) < tol):
        return x0
    else:
        return(method(f,fprime,x0-f.subs(x,x0)/fprime.subs(x,x0),tol)) #3rd input is the xn+1 estimate


inputlist = getFunc()
print(inputlist)

result = method(*inputlist)                       # the * unpacks the list
print("Estimate of the root is: " + str(result))


    
