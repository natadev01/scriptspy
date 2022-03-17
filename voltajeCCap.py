from math import e

def vCap(E,t,T):
    return(E - E*(1/e**(t/T)))

R=10000
C=1000*(10**(-6))
T=R*C
t=20
E=12
print(vCap(E,t,T))