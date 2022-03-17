
#Area del polinomio suma de Riemann
#poly(x,x0,x1,x2,...,xn)
#x es el valor de la variable
#f es x0,x1,x2,...xn
def poly(x,f):
    n = 0
    result = 0
    for i in f:
       result = i*(x**n) + result
       n = n + 1
    return result
x=3
f=[7, 2, 5, 0, 1]
print (poly(x,f))
        
