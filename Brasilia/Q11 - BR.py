import cmath
import math

cv = 3
t1 = 220
polos = 4
freq = 60
r1 = 1.22
r2 = 1.82 
x1 = 2.12
x2 = 2.12
rp = 95
xm = 98
s = 0.025
perda_vent_atrt = 25

print("\nA - Corrente no Estator\n")

z1 = complex(r1, x1)
print("z1 = ", z1,"Ohms")

zn = (complex(0,0.5*xm)*0.5*rp)/complex(0.5*rp, 0.5*xm)
print("zn = ", zn,"Ohms")

zd = zn * complex(0.5*r2/s, 0.5*x2) / (zn + complex(0.5*r2/s, 0.5*x2))
print("zd = ", zd,"Ohms")

zo = zn * complex(0.5*r2/(2-s), 0.5*x2) / (zn + complex(0.5*r2/(2-s), 0.5*x2))
print("zo = ", zo,"Ohms")

zeq = z1+zd+zo
print("zeq = ", zeq,"Ohms")

I1 = t1/zeq
print("I1 = ", I1,"A")

I1p = cmath.polar(I1)
print("I1p = ", I1p[0], "A")

print("\nB - Fator de potencia\n")

FP = cmath.cos(cmath.polar(I1)[1])
print("FP = ", FP.real)

print("\nC - Potencia de entrada\n")

p1 = t1*cmath.polar(I1)[0]*FP.real
print("P1 = ", p1,"W")

print("\nD - Potencia de saída\n")

I2d = (I1*zn)/(zn+complex(0.5*r2/s, 0.5*x2))
print("I2d = ", I2d,"A")

I2o = (I1*zn)/(zn+complex(0.5*r2/(2-s), 0.5*x2))
print("I2o = ", I2o,"A")

Pcd = (0.5*r2*(1-s)/s)*cmath.polar(I2d)[0]*cmath.polar(I2d)[0]
print("Pcd = ", Pcd,"W")

Pco = (0.5*r2*(1-s)/(2-s))*cmath.polar(I2o)[0]*cmath.polar(I2o)[0]
Pco = -Pco
print("Pco = ", Pco,"W")

Pc = Pcd+Pco
print("Pc = ", Pc,"W")

P2 = Pc-perda_vent_atrt
print("P2 = ", P2,"W")

P2_CV = P2/736
print("P2_CV = ", P2_CV,"CV")

print("\nE - Rendimento\n")
eni = (P2/p1)*100
print("eni = ", eni,"%")

print("\nF - Velocidade no eixo\n")
ns = 120*freq/polos
print("ns = ", ns,"rpm")

ws= ns*2*math.pi/60
print("ws = ", ws,"rad/s")

n = (1-s)*ns
print("n = ", n,"rpm")

w= (1-s)*ws
print("w = ", w,"rad/s")

print("\nG - Torque na carga\n")
T = P2/w
print("T = ", T,"Nm")
