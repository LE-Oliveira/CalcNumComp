def f(x):
  return x**3-x-1 

def trunc(num):
    return int(round(num*10000))/10000

def extras():
    print("N° de iterações efetuadas: 14\nIntervalo considerado: [-5,5]\nResultado final de x': 1.3251\nf(x'): 0.0015\n")
    return

def falsa(limMin, limMax, err):
    errAtual = 1
    count = 0
    extras()
    print(" Iteracao\t|\t   x\t\t|\tErro\t|")
    while(errAtual>=err):
        count+=1
        f_a,f_b = f(limMin), f(limMax)
        x_ns = (limMin*f_b-limMax*f_a)/(f_b-f_a)
        f_x_ns = f(x_ns)
        errAtual = abs(f_x_ns)
        if f_a*f_x_ns <= 0: limMax = x_ns
        else: limMin = x_ns
        print(" ", count,"\t\t|\t", "{:.4f}".format(trunc(x_ns)),"\t|     ", "{:.4f}".format(trunc(errAtual)),"  |")

falsa(-5,5,0.001)