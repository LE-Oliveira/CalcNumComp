import math as m

def c(x):
    return x/180*m.pi

def calc(t):
    S1 = m.cos(c(48)) + m.cos(c(67)) + m.cos(c(83)) + m.cos(c(108)) + m.cos(c(126))
    S2 = m.cos(c(48))**2 + m.cos(c(67))**2 + m.cos(c(83))**2 + m.cos(c(108))**2 + m.cos(c(126))**2
    S3 = 1/2.7 + 1/2 + 1/1.61 + 1/1.2 + 1/1.02
    S4 = m.cos(c(48))/2.7 + m.cos(c(67))/2 + m.cos(c(83))/1.61 + m.cos(c(108))/1.2 + m.cos(c(126))/1.02
    b = (5*S4-S1*S3)/(5*S2-S1**2)
    a = (S3 - S1*b)/5
    p = 1/a
    e = -b*p

    print(f'''
        s1 = {S1}
        s2 = {S2}
        s3 = {S3}
        s4 = {S4}
        b = {b}
        a = {a}
        p = {p}
        e = {e}
        ''')

    r = p/(1 - e*m.cos(c(t)))
    print(1-e*m.cos(c(t)))
    print(f'Theta = {t} gera um r = {r}')
    return

calc(108)