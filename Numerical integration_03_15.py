#Program for numerical integration to calculate definite integrals 

import numpy as np
import sympy as sym
x = sym.Symbol('x')  #sets x as a symbol, will use z for values and substitution later

class integral():

    def __init__(self,f,a,b,N):
    #get values from user as a list and assigns to the integral
        self.f = f
        self.a = a
        self.b = b
        self.N = N
   


    def partition(self):
        #function to initilise list called "values" of tuples (x_k,f(x_k))

        self.h = (self.b-self.a)/self.N #h is the length of each subinterval 
        print("h = "+ str(self.h))
        self.values = [] 

        z = self.a # we will move through the interval [a,b] creating each subinterval endpoint i.e. x_k + h as we progress through the loop
        # then append the tuple to the values list using a temp variable at each step
        for i in range(0,self.N+1):
            pair = []
            fz = self.f.subs(x,z)
            pair.append(z)
            pair.append(fz) 
            self.values.append(pair)
            print("Step {}, z = {}, f(z) = {}, pair = {}".format(i,z,fz,pair)) 
            z = z + self.h

        print("values of (z,f(z)) = {} ".format(self.values))    

        

    def TRAP_method1(self):
        #this will use the formula to sum the uniform spaced function values across the interval [a,b]
        #remember for values we have (z,f(z)) as the entries
        #formula is given by (h/2)*[f(z_0) + 2f(z_1) + 2f(z_2) + ... + 2f(z_(N-1))+f(z_N)] this is the approx. for the integral

        #print(len(values))
        n = len(self.values)
        print("Number of points = " + str(n))

        sum = self.values[0][1] + self.values[n-1][1] #since n is the size of the list n-1 is the final index
        print("Sum of only endpoints z_{} and z_{}: {}".format(0,n,sum))
        for i in range(1,n-1):
            sum = sum + 2*self.values[i][1]
            print("Sum of endpoints and values at point {}: {}".format(i,sum))

        self.result = self.h * 0.5 * sum  


    def simpsonsMethod_quad(self):
        #Simpson's 1/3 rule for even n (IMPORTANT)
        #this is quadratic interpolation 
        #see composite Simpson's rule online
        n = len(self.values)
        print("Number of points = " + str(n))

        sum = self.values[0][1] + self.values[n-1][1] #since n is the size of the list n-1 is the final index
        print("Sum of only endpoints z_{} and z_{}: {}".format(0,n,sum))

        for j in range(1,int(n/2)+1):
            sum = sum + 4*self.values[2*j-1][1] #this deals with the odd numbered points in partition
            print("Sum of endpoints and values at point {}: {}".format(2*j-1,sum))

        for j in range(1,int(n/2-1)+1):
            sum = sum + 2*self.values[2*j][1] #this deals with even numbered points in partition 
            print("Sum of endpoints and values at point {}: {}".format(2*j,sum)) 

        self.result = self.h * (1/3) * sum       
    

    def printResult(self):
        print("Estimate of the integral is: " + str(self.result)) 


      
def getFunc():
    #for uniform partition of the interval [a,b]
    #get values from user as a list 
    f = sym.sympify(input("Enter function: "))
    a = float(input("Enter the start of the interval, a = "))
    b = float(input("Enter the end of the interval, b = "))
    N = int(input("Enter the number of partitions N = "))
    return f,a,b,N





print("Program to evaluate a definite integral numerically.")
inputs = getFunc()

#integralTest = integral(*inputs)
#integralTest.partition()
#integralTest.TRAP_method1()
#integralTest.printResult()
#del integralTest
integralTest = integral(*inputs)
integralTest.partition()
integralTest.simpsonsMethod_quad()
integralTest.printResult()
  