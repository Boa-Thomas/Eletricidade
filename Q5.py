import cmath
import math

vlinha = 381
polos = 4
freq = 60
r1 = 0.11
R2L = 0.15
X1 = 0.17
X2L = X1
Rp = 130
Xm = 12.25

print("O rendimento a plena carga com escorregamento de 2,5%.\n")

s = 0.025
v1 = vlinha/cmath.sqrt(3)
v1real = round(v1.real,3)
print("V1 = ", v1real,"V")

Z1 = complex(r1,X1)
print("Z1 = ", Z1, "Ohm")

Z2 = complex(R2L,X2L)+(1-s)*(R2L/s)
print("Z2 = ", Z2, "Ohm")

Zn = Rp*complex(0,Xm)/complex(Rp,Xm)
print("Zn = ", Zn, "Ohm")

Zeq = Z1+((Zn*Z2)/(Zn+Z2))
print("Zeq = ", Zeq, "Ohm")

I1 = v1real/Zeq
print("I1 = ", I1, "A")
I1p = cmath.polar(I1)

print("Com I1 calculado pode-se encontrar a potencia de entrada P1")

p1= 3*v1real*I1p[0]*cmath.cos(I1p[1])
p1real = round(p1.real,3)
print("p1 = ", p1real, "W")

E1 = v1real - Z1*I1
print("E1 = ", E1, "V")

If = E1/Zn
print("If = ", If, "A")

I2 = E1/Z2
print("I2 = ", I2, "A")

p2 = 3*(1-s)*(R2L/s)*I2*I2
p2real = round(p2.real,3)
print("p2 = ", p2real, "W")

eni = p2real/p1real*100
eni = round(eni,3)
print("eni = ", eni, "%")

print("O torque nesta condiçao. \nA velocidade sí ncrona e a rotaça o do motor sa o calculadas por:")
ns = 120*freq/polos
print("ns = ", ns, "rpm")

n = (1-s)*ns
print("n = ", n, "rpm")

print("A velocidade angular do motor sera :")

w= n*2*math.pi/60
w = round(w,3)
print("w = ", w, "rad/s")

t = p2real/w
treal = round(t.real,3)
print("t = ", treal, "Nm")