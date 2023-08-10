def f(x,y):
    return(1+x**2)/(x**2*y**2)

def fReal(x):
    return ((3*x**2-3+8*x)/x)**(1/3)

def RungeKutta(min, max, i):
    h = (max-min)/i
    x0, y0 = 1,2
    print(f"x0 = 1\t\t|\ty0 = 2\t\t|\tErro = {abs((y0-fReal(x0))/fReal(x0)):.4f}")
    for i in range(0,i):
        k1 = f(x0, y0)
        k2 = f(x0+h, y0+h*k1)
        y = y0 + (h/2)*(k1+k2)
        x = x0 + h
        fR = fReal(x)
        err = abs((y-fR)/fR)
        print(f"x{i+1} = {x}\t|\ty{i+1} = {y:.4f}\t|\tErro = {err:.4f}")
        y0, x0 = y, x
    return

print("\nRunge Kutta Ordem 2 com 4 iterações\n")
RungeKutta(1,2,4)
print("\nRunge Kutta Ordem 2 com 8 iterações\n")
RungeKutta(1,2,8)
print('\n')
