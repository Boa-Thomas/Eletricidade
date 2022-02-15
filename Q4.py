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

print("a) os para metros a considerar o circuito ele trico equivalente da Figura 2. \n Antes de qualquer ca lculo direto dos para metros tem-se que calcular os valores por fase dos ensaios, pois alguns para metros sa o trifa sicos")

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

print("A - Qual a pote ncia no eixo da ma quina se alimentado com tensa o nominal em conexa o Y e com escorregamento de 1,5 %?")

s = 0.015

v1 = t2
print("v1 = ", v1,"V")

Zn = Rp*complex(0,xm)/(complex(Rp,xm))
print("Zn = ", Zn,"Ohm")

Z1 = complex(R1,X1)
print("Z1 = ", Z1,"Ohm")

Z2 = complex(R2L,X2L)+(1-s)*R2L/s
print("Z2 = ", Z2,"Ohm")

Zeq = Z1+((Zn*Z2)/(Zn+Z2))
print("Zeq = ", Zeq,"Ohm")

I1 = v1/Zeq
print("I1 = ", I1,"A")
I1p = cmath.polar(I1)

print("Com I1 calculado pode-se encontrar a pote ncia de entrada P")

p1=3*v1*I1p[0]*cmath.cos(I1p[1])
p1real = round(p1.real,3)
print("p1 = ", p1real,"W")

E1 = v1 - Z1*I1
print("E1 = ", E1,"V")

If = E1/Zn 
print("If = ", If,"A")

I2 = E1/Z2
print("I2 = ", I2,"A")

P2 = 3*(1-s)*(R2L/s)*I2*I2
p2real = round(P2.real,3)
print("P2 = ", p2real,"W")

print("Qual o rendimento para a condiça o do item anterior?")

eni = p2real/p1real*100
eni = round(eni,3)
print("eni = ", eni,"%")

print("Para a mesma condiçao o torque no eixo da maquina.\nA velocidade síncrona e a rotaçao do motor sa o calculadas por:")
ns = 120*freq/polos
print("ns = ", ns,"rpm")

n = (1-s)*ns
print("n = ", n,"rpm")

print("A velocidade angular do motor será")
w = n*2*math.pi/60
print("w = ", w,"rad/s")

T = p2real/w
print("T = ", T,"N.m")