from MathematicsOperationsOnFunctions import functionDerived,functionIntegral,functionDivide,functionSubtraction,functionMultiply,functionSum
from InputData import InputData
import numpy as np
import matplotlib.pyplot as plt
from functools import partial
import scipy.integrate as si

data = InputData()
N = data.N

#Could be helpful:
#Exponential function: np.exp(x)
#Logarithm function: np.log(x)
functionA = lambda x: 1
functionB = lambda x: 0
functionC = lambda x: 0
functionF = lambda x: 0

H = []
rightSite = []
leftSite = []
step = (data.endPoint-data.startPoint)/(N-1)

#Pyramids generation
for i in range(0,N,1):
    H.append(partial(lambda i,x: (((1/(step*i - step*(i-1)))*x - step*(i-1)/(step*i - step*(i-1))) if (x < step*i and x > step*(i-1)) else (((step*(i+1)/(step*(i+1)-step*i))-x*(1/(step*(i+1)-step*i))) if (x >= step*i and x< step*(i+1)) else 0.0)),i))

#shift
shift =  lambda x: data.Ur*H[N-1](x)

#Filling Right site
for i in range(0,N-1,1):
    rightSite.append(si.quad(functionMultiply(H[i],functionF),data.startPoint,data.endPoint)[0] - data.gamma*H[i](0)
    )
rightSite.append(data.Ur)

#Filling Left Site
for i in range(0,N-1,1):
    row = []
    for j in range(0,N,1):
        row.append(
            (-1)*si.quad(functionMultiply(functionMultiply(functionDerived(H[i]),functionDerived(H[j])),functionA),data.startPoint,data.endPoint)[0]
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

L = np.array(leftSite)
R = np.array(rightSite)

u = np.linalg.solve(L,R)

print("B(u*,v) matrix:")
print(L)

print("l(v) matrix:")
print(R)

print("Result matrix:")
print(u)

linearCombination = []
for i in range(0,N,1):
    linearCombination.append(functionMultiply(H[i],lambda x: u[i]))

#Showing result
X = []
Y = []
for j in np.arange(data.startPoint,data.endPoint + 0.001,0.001):
    X.append(round(j,4))
    value = 0
    for i in range(0,N,1):
        value += linearCombination[i](j)
    Y.append(round(value,4))

#Plotting the points
plt.plot(X,Y)

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.title('Output Function')

#Function to show the plot
plt.show()