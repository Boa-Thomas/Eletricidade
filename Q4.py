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
print("X1 = ", X1,"Ohm")

print("A - Qual a pote ncia no eixo da ma quina se alimentado com tensa o nominal em conexa o Y e com escorregamento de 1,5 %?")

s = 0.015