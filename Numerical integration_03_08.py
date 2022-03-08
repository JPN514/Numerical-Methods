#Program for numerical integration to calculate definite integrals 

import numpy as np
import sympy as sym
x = sym.Symbol('x')  #sets x as a symbol, will use z for values and substitution later


def TRAP_getFunc():
    #specific for trapezium rule with uniform partition of the interval [a,b]
    #get values from user as a list 
    print("Program to evaluate a definite integral numerically.")
    f = sym.sympify(input("Enter function: "))
    a = float(input("Enter the start of the interval, a = "))
    b = float(input("Enter the end of the interval, b = "))
    N = int(input("Enter the number of partitions N = "))
    return f,a,b,N


def TRAP_list(f,a,b,N):
    #function to initilise list called "values" of tuples (x_k,f(x_k))

    h = (b-a)/N #h is the length of each subinterval 
    print("h = "+ str(h))
    values = [] 

    z = a # we will move through the interval [a,b] creating each subinterval endpoint i.e. x_k + h as we progress through the loop
    # then append the tuple to the values list using a temp variable at each step
    for i in range(0,N+1):
        pair = []
        fz = f.subs(x,z)
        pair.append(z)
        pair.append(fz) 
        values.append(pair)
        print("Step {}, z = {}, f(z) = {}, pair = {}".format(i,z,fz,pair)) 
        z = z + h

    print("values of (z,f(z)) = {} ".format(values))    

    return values, h

def TRAP_method1(values,h):
    #this will use the formula to sum the uniform spaced function values across the interval [a,b]
    #remember for values we have (z,f(z)) as the entries
    #formula is given by (h/2)*[f(z_0) + 2f(z_1) + 2f(z_2) + ... + 2f(z_(N-1))+f(z_N)] this is the approx. for the integral

    #print(len(values))
    n = len(values)
    print("Number of points = " + str(n))

    sum = values[0][1] + values[n-1][1] #since n is the size of the list n-1 is the final index
    print("Sum of only endpoints z_{} and z_{}: {}".format(0,n,sum))
    for i in range(1,n-1):
        sum = sum + 2*values[i][1]
        print("Sum of endpoints and values at point {}: {}".format(i,sum))

    result = h * 0.5 * sum   

    return result


def TRAP_integral():
    inputs = TRAP_getFunc() #gets function, interval and number of subintervals from user
    partition = TRAP_list(*inputs) #turns the input into the required function values and steps needed
    integral = TRAP_method1(*partition)  #method to compute the result 
    return integral 


integral = TRAP_integral()
print("Estimate of the integral using trapezium rule is: " + str(integral))   





