# if __name__ == '__main__':
#     print("Hello World")

def f(x):
    a,b,c = (1,0,-3)
    return (a*pow(x,2)+b*x+c)

def bisec():
    limMin, limMax, err, errAtual = (1,2,0.01,1)
    while(errAtual>=err):
        x_ns = (limMin + limMax)/2
        f_x_ns = f(x_ns)
        if f_x_ns<=0:
            limMin = x_ns
        else:
            limMax = x_ns
        errAtual = abs(limMax-limMin)/2
    print("A raiz encontrada foi:" + str(x_ns))

bisec()
