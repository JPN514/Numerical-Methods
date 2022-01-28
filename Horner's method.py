#Program for polynomial evalution using Horner's Method
#Evaluates the poly at a given point x0 using recursion

def getPoly():
    #gets the degree and the coefficients of the polynomial 
    n = int(input("Enter the degree of the polynomial f(x): "))
    text = "Enter the integer coefficents of the polynomial in order a_n, a_n-1, ..., a0 each separated by a comma: "
    coeffs = list(map(int,input(text).split(","))) #gets the coefficients as a list
    point = int(input("Enter x0 the point for f(x) to be evaluated at: "))
    return n,coeffs,point

def listprep(coeffs):
    #function to prepare the new coefficient list
    bi = []
    bi.append(coeffs[0]) # this defines b_n == a_n
    return bi     

def Horner(degree, ai, bi, point):
    #We will define a new list of coeffs b_i by recursion
    #using the definition b_n := a_n, b_n-1 := a_n-1 + b_n*x0, ... b_0 := a_0 + b_1*x0

    if degree == 0:
        return bi
    else:
        newcoeff = int(ai[degree-1]) + int(bi[len(bi)-1]*point)
        print("newcoeff: {}, ai[deg-1]: {}, bi[len(bi)-1]: {}, x0 = {}".format(newcoeff,int(ai[degree-1]),int(bi[len(bi)-1]*point),point))
        bi.append(newcoeff)
        print("Iteration: {}, bi = {}, {}".format(degree,bi, bi[len(bi)-1]))
        return Horner(degree-1,ai,bi,point)    



    return 

poly = list(getPoly()) #poly is a list containing the degree and the coefficients list
print(poly)
bi = listprep(poly[1]) #poly[1] is the coeffs list
print(bi)
poly.insert(2,bi) #puts the bi list into the third position in the poly list
poly[1].reverse()
print("Updated: {}".format(poly))
result = Horner(*poly)


print(result[len(result)-1])



