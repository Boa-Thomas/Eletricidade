import cmath
import math
from tkinter import W, Wm

potencia = 375000
vlinha = 2200
polos =12
freq = 60
#ao girar a vazio com tensão e freq nominais absorve:
current = 20
potency = 14000
#por fase

R1 = 0.4
R2L = 0.2
X1 = 2.0
X2L = X1
s = 0.02 #escorregamento
print("\nA - Corrente no estator\n")

Vf = vlinha/cmath.sqrt(3)
Vfreal = round(Vf.real,3)
print("Vf = ", Vfreal, "V")

Rp = Vf*Vf/potency
Rpreal = round(Rp.real,3)
print("Rp = ", Rpreal, "Ohm")

Xm = Vfreal*Vfreal/cmath.sqrt((Vfreal*current)*(Vfreal*current)-potency*potency)
Xmreal = round(Xm.real,3)
print("Xm = ", Xmreal, "Ohm")

Zn = Rp*complex(0,Xm)/complex(Rp,Xm)
print("Zn = ", Zn, "Ohm")

Z2= R2L/s+complex(0,X2L)
print("Z2 = ", Z2, "Ohm")

Z1 = R1+complex(0,X1)
print("Z1 = ", Z1, "Ohm")

Zeq1 = Zn*Z2/(Zn+Z2)
print("Zeq1 = ", Zeq1, "Ohm")

Zeq2 = Z1+Zeq1
print("Zeq2 = ", Zeq2, "Ohm")

I1 = Vfreal/Zeq2
print("I1 = ", I1, "A")

print("\nB - Fator de pontecia\n")

I1p = cmath.polar(I1)
print("I1p = ", I1p)

FP = cmath.cos(I1p[1])
print("FP = ", FP)

print("\nC - Potencia de entrada\n")
Pe = 3*Vfreal*I1p[0]*cmath.cos(I1p[1])
Pereal = round(Pe.real,3)
print("Pe = ", Pereal, "W")

print("\nD - Corrente de saida\n")
E1 = Vfreal - Z1*I1
print("E1 = ", E1, "V")

I2L = E1/Z2
print("I2L = ", I2L, "A")

print("\nE - Potencia de saida\n")
I2Lp = cmath.polar(I2L)

Ps= 3*(1-s)*(R2L/s)*I2Lp[0]*I2Lp[0]
Psreal = round(Ps.real,3)
print("Ps = ", Psreal, "W")

print("\nF - Velocidade da carga\n")
ns = 120*freq/polos
print("ns = ", ns, "rpm")

ws = ns*2*math.pi/60
ws = round(ws,3)
print("ws = ", ws, "rad/s")

n = (1-s)*ns
print("n = ", n, "rpm")

w=2*math.pi*n/60
w = round(w,3)
print("w = ", w, "rad/s")

print("\nG - Torque na carga\n")
Td = Ps/w
print("Td = ", Td, "Nm")

print("H - Rendimento")
eni = Ps/Pe*100
print("eni = ", eni, "%")
