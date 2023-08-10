def f(x):
    return x**3-x-1

def f_(x):
    return 3*x**2-1

def trunc(num):
    return (int(round(num*10000)))/10000

def extras():
    print("f'(x): 3x²-1\nf''(x): 6x\nN° de iterações efetuadas: 20\nValor Inicial(x0): 0\nResultado final de x': 1.3247\nf(x'): 0.0009\n")
    return

def newton():
    x0 = 0
    count = 1
    err = 1
    x = x0-f(x0)/f_(x0)
    print(" Iteracao\t|\t   x\t\t|\tErro\t|")
    print(" ", count,"\t\t|\t", "{:.4f}".format(trunc(x)),"\t|     ", "{:.4f}".format(trunc(abs(x-x0))),"  |")
    while (err>0.001):
        x_ant = x
        x = x-f(x)/f_(x)
        count+=1
        err = abs(x-x_ant)
        print(" ", count,"\t\t|\t", "{:.4f}".format(trunc(x)),"\t|     ", "{:.4f}".format(trunc(abs(x-x_ant))),"  |")
    print("f'1(x): 3x²-1\nf''(x): 6x\nN° de iterações efetuadas: ", count, "\nValor Inicial(x0):", x0, "\nResultado final de x':","{:.4f}".format(trunc(x)),"\nf(x'): ","{:.4f}".format(trunc(abs(x-x_ant))))
    return

newton()
