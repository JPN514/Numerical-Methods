#Program for numerical integration to calculate definite integrals 
import math
import numpy as np
import sympy as sym
x = sym.Symbol('x')  #sets x as a symbol, will use z for values and substitution later

class integral():

    def __init__(self,f,a,b,N):
    #get values from user as a list and assigns to the integral
        self.f = sym.sympify(f) #attmept to get trig and ln fucntions to be recognised ???
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
        #this is quadratic interpolation composite version
        #see composite Simpson's rule online
        n = len(self.values)
        print("Number of points = " + str(n))

        sum = self.values[0][1] + self.values[n-1][1] #since n is the size of the list n-1 is the final index
        print("Sum of only endpoints z_{} and z_{}: {}".format(0,n,sum))

        for j in range(1,int(n/2)+1):
            sum = sum + 4*self.values[2*j-1][1] #this deals with the odd numbered points in partition
            print("Sum of endpoints and values up to and including point {}: {}".format(2*j-1,sum))

        for j in range(1,int(n/2-1)+1):
            sum = sum + 2*self.values[2*j][1] #this deals with even numbered points in partition 
            print("Sum of endpoints and values up to and including point {}: {}".format(2*j,sum)) 

        self.result = self.h * (1/3) * sum 


    def simpsonsMethod_cubic(self):
        #Simpson's 3/8 rule composite version, cubic interpolation
        #Here n is a multiple of 3 
        #the subintervals still have uniform length 

        n = len(self.values)
        print("Number of points = " + str(n))

        sum = self.values[0][1] + self.values[n-1][1] #since n is the size of the list n-1 is the final index
        print("Sum of only endpoints z_{} and z_{}: {}".format(0,n,sum))

        for j in range(1,int(n-1)):
            if (j % 3 == 0):
                continue #ensures skip the positions which are multiples of 3
            sum = sum + 3*self.values[j][1] #this deals with the non multiple of 3 numbered points in partition
            print("Sum of endpoints and values up to and including point {}: {}".format(j,sum))

        for j in range(1,int(n/3)):
            sum = sum + 2*self.values[3*j][1] #this deals with points in partition whose positions are multiples of 3  
            print("Sum of endpoints and values up to and including point {}: {}".format(3*j,sum)) 

        self.result = self.h * (3/8) * sum 

        return          
    

    def printResult(self):
        print("Estimate of the integral is: " + str(self.result)) 


class integral_irreg(integral): 
    def __init__(self,f,a,b,N,min_h,max_h):
    #get values from user as a list and assigns to the integral
        self.f = sym.sympify(f) #attmept to get trig and ln fucntions to be recognised ???
        self.a = a
        self.b = b
        self.N = N
        self.min = min_h
        self.max = max_h #max and min used to determine the variable partition gaps

    def partition(self):
        #function to initilise list called "values" of tuples (x_k,f(x_k))

        self.values = [] 
        self.h = []

        z = self.a # we will move through the interval [a,b] creating each subinterval endpoint i.e. x_k + h as we progress through the loop
        # then append the tuple to the values list using a temp variable at each step
        for i in range(0,self.N):
            pair = []
            fz = self.f.subs(x,z)
            pair.append(z)
            pair.append(fz) 
            self.values.append(pair)
            print("Step {}, z = {}, f(z) = {}, pair = {}".format(i,z,fz,pair)) 
            h_i = self.b
            while (z + h_i >= self.b):
                h_i = self.get_h()
            z = z + h_i
            self.h.append(h_i)

        fz = self.f.subs(x,self.b) #deal with the final point on its own 
        pair = []
        pair.append(self.b)
        pair.append(fz)  
        self.values.append(pair)    


        print("values of (z,f(z)) = {} ".format(self.values))
        return   

    def get_h(self): 
        #generates a random distance for the partition gap
        h_i = round(np.random.uniform(self.min,self.max),4)
        return h_i


    def simpsonsIrreg(self):
        #Simpson's rule for a non-uniform partition of interval [a,b]
        #for even number N of subintervals

        n = len(self.values)
        print("Number of points = " + str(n))

        sum = 0
        for i in range(0,int(n/2)):
            h_i = (self.h[2*i]+self.h[2*i+1])/6
            A = (2-(self.h[2*i+1]/self.h[2*i]))*self.values[2*i][1]
            B = ((self.h[2*i]+self.h[2*i+1])**2/(self.h[2*i]*self.h[2*i+1]))*self.values[2*i+1][1]
            C = (2-(self.h[2*i]/self.h[2*i+1]))*self.values[2*i+1][1]

            sum = sum + h_i*(A+B+C)

        self.result = sum
        return    




      
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
#integralTest = integral(*inputs)
#integralTest.partition()
#integralTest.simpsonsMethod_quad()
#integralTest.printResult()
#integralTest = integral(*inputs)
#integralTest.partition()
#integralTest.simpsonsMethod_cubic()
#integralTest.printResult()

integralTest = integral_irreg(*inputs,0.5,1.5)
integralTest.partition()
integralTest.simpsonsIrreg()
integralTest.printResult()
