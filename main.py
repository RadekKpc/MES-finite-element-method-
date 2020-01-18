from MathematicsOperationsOnFunctions import functionDerived,functionIntegral,functionDivide,functionSubtraction,functionMultiply,functionSum
from InputData import InputData
import numpy as np
import matplotlib.pyplot as plt
from functools import partial
import scipy.integrate as si

data = InputData()
N = data.N

#Exponential function: np.exp(x)
#Logarithm function: np.log(x)
functionA = lambda x: 9*np.exp(x)
functionB = lambda x: 2*x + x*x + 2
functionC = lambda x: 30*x + 4*np.log(x)
functionF = lambda x: 4*x

H = []
rightSite = []
leftSite = []
step = (data.endPoint-data.startPoint)/(N-1)

#Pyramids generation
for i in range(0,N,1):
    H.append(partial(lambda i,x: (((1/(step*i - step*(i-1)))*x - step*(i-1)/(step*i - step*(i-1))) if (x < step*i and x > step*(i-1)) else (((step*(i+1)/(step*(i+1)-step*i))-x*(1/(step*(i+1)-step*i))) if (x >= step*i and x< step*(i+1)) else 0.0)),i))

#shift shift
shift =  lambda x: data.Ur*H[N-1](x)


# Filling Right site
for i in range(0,N-1,1):
    rightSite.append(si.quad(functionMultiply(H[i],functionF),data.startPoint,data.endPoint)[0] - data.gamma*H[i](0))
rightSite.append(data.Ur)

# Filling Left Site
for i in range(0,N-1,1):
    row = []
    for j in range(0,N,1):
        row.append(
            si.quad(functionMultiply(functionMultiply(functionDerived(H[i]),functionDerived(H[j])),functionA),data.startPoint,data.endPoint)[0]
            +si.quad(functionMultiply(functionMultiply(functionDerived(H[i]),H[j]),functionB),data.startPoint,data.endPoint)[0]+
            si.quad(functionMultiply(functionMultiply(H[i],H[j]),functionC),data.startPoint,data.endPoint)[0]
            - data.beta*H[i](0)*H[j](0)
        )
    leftSite.append(row)

row = []
for j in range(0,N-1,1):
    row.append(0)
row.append(1)
leftSite.append(row)

# print("Equations: ")
# print(leftSite)
# print(rightSite)

L = np.array(leftSite)
R = np.array(rightSite)

# print("Equations in np:")
# print(L)
# print(R)

u = np.linalg.solve(L,R)
# print(u)

linearCombination = []
for i in range(0,N,1):
    linearCombination.append(functionMultiply(H[i],lambda x: u[i]))

# Showing result
E1 = []
E1args = []
for j in np.arange(0.0,1.0,0.01):
    E1.append(j)
    value = 0
    for i in range(0,N,1):
        value += linearCombination[i](j)
    E1args.append(value + shift(j))
plt.plot(E1,E1args)
plt.show()