def interpolacao():
    tabela = {'20': '0.99907',
            '25': '0.99852',
            '30': '0.99826',
            '35': '0.99818',
            '40': '0.99828',
            '45': '0.99849',
            '50': '0.99878',
            '55': '0.99919'}
    n = len(tabela)-1

    return

def teste(inte, v):
    tabela = []
    for i in range (2):
        x = float(input())
        aux = 10*x**4+2*x+1
        t = (x, aux)
        tabela.append(t)
    coef = (tabela[1][1]-tabela[0][1])/(tabela[1][0]-tabela[0][0])
    print("Coef", coef)
    print("Interpolacao", 1+(v)*2.15)
    print("Real", 10*v**4+2*v+1)
    return

teste(2, 0.15)