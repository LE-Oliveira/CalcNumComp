def f(x):
    return x**3-x-1 

def trunc(num):
    return int(round(num*10000))/10000

def extras():
    print("N° de iterações estipulado: 13.2877\nN° de iterações efetuadas: 14\nIntervalo considerado: [-5,5]\nResultado final de x': 1.3251\nf(x'): 0.0015\n")
    return

def bisec():
    limMin, limMax, err, errAtual = (-5,5,0.001,1)
    count = 0
    extras()
    print(" Iteracao\t|\t   x\t\t|\tErro\t|")
    while(errAtual>=err):
        count+=1
        x_ns = (limMin + limMax)/2
        f_x_ns = f(x_ns)
        errAtual = abs(limMax-limMin)/2
        if f_x_ns<=0:
            limMin = x_ns
        else:
            limMax = x_ns
        print(" ", count,"\t\t|\t", "{:.4f}".format(trunc(x_ns)),"\t|     ", "{:.4f}".format(trunc(errAtual)),"  |")

bisec()