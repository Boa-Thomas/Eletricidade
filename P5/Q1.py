import cmath
import math
from tkinter import W


polos = 8
freq = 60
t1 = 380
t2 = 220
r1 = 0.19
r2L = 0.11
x1 = 0.45
x2L = 0.21
rp = 130
xm = 22
perdastotais = 1735
rpm = 400


ns = 120*freq/polos
print("ns = ", ns)
s = (ns - rpm)/ns
print("s = ", s)

aux1=[x1+x2L]
Zs = complex(r1+r2L/s,sum(list(aux1)))
print("Zs = ", Zs)

Zsp = cmath.polar(Zs)
print("Zsp = ", Zsp)

Zp = rp*complex(0,xm)/complex(rp,xm)
print("Zp RECTANGULAR = ", Zp)

Zpp = cmath.polar(Zp)
print("Zp POLAR = ", Zpp)

I2 = complex(t2,0)/Zs
print("I2 RECT= ", I2)
I2p = cmath.polar(I2)
print("I2 POLAR= ", I2p)

If = complex(t2,0)/Zp
print("If RECT= ", If)

I1 = I2 + If
print("I1 RECT= ", I1)
I1p = cmath.polar(I1)
print("I1 POLAR= ", I1p)

print("\nA - a corrente de entrada\n")
Zeq = (Zs*Zp)/(Zs+Zp)
print("Zeq RECT= ", Zeq)
cmath.polar(Zeq)
print("Zeq POLAR= ", Zeq)

print("\nB - A potencia consumida da rede\n")
p1 = 3*t2*I1p[0]*cmath.cos(I1p[1])
p1real = round(p1.real,4)
print("p1 = ", p1real,"W")

print("\nC - A potencia no eixo da maquina\n")
p2 = 3*(1-s)*(r2L/s)*(I2p[0])*(I2p[0])
p2 = round(p2,4)
print("p2 =", p2,"W")

print("\nD - O torque no eixo da maquina\n")
w = 2*cmath.pi*rpm/freq
w = round(w,4)
print("w = ", w,"rad/s")

t=p2/w
t = round(t,4)
print("t = ", t,"N.m")

print("\nE - rendimento\n")
eni = (p2/p1real)*100
eni = round(eni,4)
print("eni = ", eni,"%")