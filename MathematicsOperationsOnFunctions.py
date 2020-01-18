
# basic mathematic functions

def functionSum(fun1,fun2):
    return lambda x: fun1(x) + fun2(x)

def functionMultiply(fun1,fun2):
    return lambda x: fun1(x)*fun2(x)

def functionSubtraction(fun1,fun2):
    return lambda x: fun1(x) - fun2(x)

def functionDivide(fun1,fun2):
    return lambda x: fun1(x) / fun2(x)

def functionDerived(fun):
    precision = 0.000001
    return lambda x: (fun(x + precision) - fun(x))/precision

def functionIntegral(fun,start,stop,step):
    result = 0.0
    m = start
    counter =0
    while(m <= stop):
        result+=(fun(m))
        m+=step
        counter+=1
    return (stop - start)*result/counter




