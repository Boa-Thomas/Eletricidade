import cmath
import math

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
print("Corrente no estator")

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
