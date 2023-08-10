def f(t,y):
    return(1+t**2)/(t**2*y**2)

def fReal(t):
    return ((3*t**2-3+8*t)/t)**(1/3)

def Euler(min, max, i):
    h = (max-min)/i
    x0, y0 = 1,2
    print(f"x0 = 1\t\t|\ty0 = 2\t\t|\tErro = {(y0-fReal(x0))/fReal(x0):.4f}")
    for i in range(0,i):
        fx = f(x0,y0)
        y = y0 + h*fx
        x = x0+h
        fR = fReal(x)
        err = abs((y-fR)/fR)
        print(f"x{i+1} = {x}\t|\ty{i+1} = {y:.4f}\t|\tErro = {err:.4f}")
        y0, x0 = y, x
    return

print("\nEuler com 4 iterações\n")
Euler(1,2,4)
print("\nEuler com 8 iterações\n")
Euler(1,2,8)
print('\n')