import numpy as np
import sympy as sym
t = sym.Symbol('t')  #sets t as a symbol
s = sym.Symbol('s') 
y = sym.Symbol('y')


def get_inputs():

    y_prime = sym.sympify(input("Enter function y'(t): "))
    t_0 = float(input("Enter t_0: "))
    y_0 = float(input("Enter the initial conditions, y(t_0)="))
    
    return y_prime,y_0,t_0

def assign_phi(t_0,y_0,phi_k):

    phi_k1 = y_0 + sym.integrate(phi_k,(t,t_0,t)) #iterative step, note use t as variable else this throws an error

    return phi_k1

def Picards_iteration():
    inputs = get_inputs()
    y_prime = inputs[0]
    phi_0 = inputs[1] #assigns phi_0(t)=y_0
    t_0 = inputs[2]
    steps = int(input("Enter the number of steps: "))
    phi_k1 = phi_0 #to allow for initial step

    for i in range(steps):
        phi_k = y_prime.subs(y,phi_k1) #to assign for next iteration
        #print(phi_k)
        phi_k1 = assign_phi(t_0,phi_0,phi_k) 

    print(phi_k1)

Picards_iteration()

#print(sym.integrate(y,(t,0,s)))