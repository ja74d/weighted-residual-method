import numpy as np
import math
import sympy as sp

# (d^2/dx^2)(phi) + (d/dx)(phi) + (phi) + p = 0
# (d^2/dx^2)phi - phi = 0


# (bcx[0], bcy[0])
# (bcx[1], bcy[1])
bcx = [0, 1]
bcy = [0, 1]

x1 = np.linspace(0, 1, 100)

n = 2

x = []

for i in x1:
    x.append(float(i))

#print(type(x))

# ksi is the function that satisfies the essensial boundry conditions
def ksi():
    m = (bcy[1]-bcy[0])/(bcx[1]-bcx[0])
    func = []
    for j in x:
        phi = m*(j - bcx[0]) + bcy[0]
        func.append(phi)
    
    if bcx[0] == 0 and bcy[0]==0:
        eq = f'{m}(x)'
    elif bcx[0] == 0:
        eq = f'{m}(x) + {bcy[0]}'
    elif bcy[0] == 0:
        eq = f'{m}(x - {bcx[0]})'
    

    #print(f'{m}(x - {bcx[0]}) + {bcy[0]}')
    print(eq)
    global ksi
    ksi = eq

ksi()


#approximate function

# Define the symbolic variable and function
x = sp.symbols('x')

f = sp.sin(sp.pi * x)
c = sp.pi

# Calculate the derivative-second derivative-first derivative
s_d = sp.diff(sp.diff(f, x))
f_d = sp.diff(f, x)

# Display the result
# print("Original function:", f)

L = s_d - 1
print(L)