from MathematicsOperationsOnFunctions import functionDerived,functionIntegral,functionDivide,functionSubtraction,functionMultiply,functionSum
from InputData import InputData
import numpy as np
import matplotlib.pyplot as plt
from functools import partial

data = InputData()
N = data.N
step = (data.endPoint-data.startPoint)/(N-1)
H = []

lambdas = [partial(lambda x: x, i) for i in range(3)]

for i in range(0,N,1):
    print( i*step)

#Generowanie piramidek
for i in range(0,N,1):
    H.append(partial(lambda i,x: (((1/(step*i - step*(i-1)))*x - step*(i-1)/(step*i - step*(i-1))) if (x < step*i and x > step*(i-1)) else (((step*(i+1)/(step*(i+1)-step*i))-x*(1/(step*(i+1)-step*i))) if (x >= step*i and x< step*(i+1)) else 0.0)),i))


for f in H:
    E1 = []
    E1args = []
    for j in np.arange(0.0,1.0,0.01):
        E1.append(j)
        E1args.append(functionDerived(f)(j))
    plt.plot(E1,E1args)
    plt.show()




