# if __name__ == '__main__':
#     print("Hello World")

def f(x):
    a = 1
    b = 0
    c = 0
    return (a*pow(x,2)+b*x+c)

def bisec():
    err = 0.0001
    limMin = -1
    limMax = 1
    errAtual = 1
    while(errAtual>=err):
        x_ns = (limMin + limMax)/2
        f_x_ns = f(x_ns)
        if f_x_ns<=0:
            limMin = x_ns
        else:
            limMax = x_ns
        errAtual = abs(limMax-limMin)/2
    print(x_ns)

bisec()
