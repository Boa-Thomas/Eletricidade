import cmath
import math

cv = 50
polos = 2
freq = 60
t1 = 380
t2 = 220
#vazio
vo=220
io=17
p3 = 1630
pva = 530
#bloqueado
vb= 29.5
ib= 55.7
p3b = 2615
rcc = 0.1

print("\na) os para metros a considerar o circuito ele trico equivalente da Figura 2. \n Antes de qualquer ca lculo direto dos para metros tem-se que calcular os valores por fase dos ensaios, pois alguns para metros sa o trifasicos \n")

po= (p3-pva)/3
po= round(po,3)
print("po = ", po,"W")

Rp = vo*vo/po
Rp = round(Rp,3)
print("Rp = ", Rp,"Ohm")

xm = (vo*vo)/cmath.sqrt((vo*io)*(vo*io)-po*po)
xm = round(xm.real,3)
print("xm = ", xm,"Ohm")

print("Do ensaio de rotor bloqueado:")

pb = p3b/3
pb = round(pb,3)
print("pb = ", pb,"W")

Re = pb/(ib*ib)
Re = round(Re,3)
print("Re = ", Re,"Ohm")

R1 = rcc
print("R1 = ", R1,"Ohm")

R2L = Re-R1
R2L = round(R2L,3)
print("R2L = ", R2L,"Ohm")

Xe = cmath.sqrt(((vb*ib)*(vb*ib))-(pb*pb))/(ib*ib)
Xe = round(Xe.real,3)
print("Xe = ", Xe,"Ohm")

X1 = Xe/2
X1 = round(X1,3)
X2L = X1
print("X1 = ", X1,"Ohm")

print("\nA - Qual a potencia no eixo da ma quina se alimentado com tensa o nominal em conexa o Y e com escorregamento de 1,5 %?\n")

s = 0.015

v1 = t2
print("v1 = ", v1,"V")

Zn = Rp*complex(0,xm)/(complex(Rp,xm))
Znaux1 = round(Zn.real,3)
Znaux2 = round(Zn.imag,3)
Zn = complex(Znaux1,Znaux2)
print("Zn = ", Zn,"Ohm")

Z1 = complex(R1,X1)
print("Z1 = ", Z1,"Ohm")

Z2 = complex(R2L,X2L)+(1-s)*R2L/s
Z2aux1 = round(Z2.real,3)
Z2aux2 = round(Z2.imag,3)
Z2 = complex(Z2aux1,Z2aux2)
print("Z2 = ", Z2,"Ohm")

Zeq = Z1+((Zn*Z2)/(Zn+Z2))
Zeqaux1 = round(Zeq.real,3)
Zeqaux2 = round(Zeq.imag,3)
Zeq = complex(Zeqaux1,Zeqaux2)
print("Zeq = ", Zeq,"Ohm")

I1 = v1/Zeq
I1aux1 = round(I1.real,3)
I1aux2 = round(I1.imag,3)
I1 = complex(I1aux1,I1aux2)
print("I1 = ", I1,"A")
I1p = cmath.polar(I1)

print("\nCom I1 calculado pode-se encontrar a pote ncia de entrada P\n")

p1=3*v1*I1p[0]*cmath.cos(I1p[1])
p1real = round(p1.real,3)
print("p1 = ", p1real,"W")

E1 = v1 - Z1*I1
E1aux1 = round(E1.real,3)
E1aux2 = round(E1.imag,3)
E1 = complex(E1aux1,E1aux2)
print("E1 = ", E1,"V")

If = E1/Zn
Ifaux1 = round(If.real,3)
Ifaux2 = round(If.imag,3)
If = complex(Ifaux1,Ifaux2)
print("If = ", If,"A")

I2 = E1/Z2
I2aux1 = round(I2.real,3)
I2aux2 = round(I2.imag,3)
I2 = complex(I2aux1,I2aux2)
print("I2 = ", I2,"A")

P2 = 3*(1-s)*(R2L/s)*I2*I2
p2real = round(P2.real,3)
print("P2 = ", p2real,"W")

print("\nQual o rendimento para a condiça o do item anterior?\n")

eni = p2real/p1real*100
eni = round(eni,3)
print("eni = ", eni,"%")

print("\nPara a mesma condiçao o torque no eixo da maquina.\nA velocidade síncrona e a rotaçao do motor sa o calculadas por:\n")
ns = 120*freq/polos
print("ns = ", ns,"rpm")

n = (1-s)*ns
print("n = ", n,"rpm")

print("\nA velocidade angular do motor será\n")
w = n*2*math.pi/60
print("w = ", w,"rad/s")

T = p2real/w
print("T = ", T,"N.m")