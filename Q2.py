import cmath
import math
from re import I

from Q1 import Zeq


polos = 4
freq = 60
#Ensaio a vazio
Vl=381
p=1700
i=18.1
Pva=575
#Ensaio de rotor bloqueado
Vlblock=41.2
pblock=2634
iblock=59.1
Rblock=0.1
print("os parametros do motor de induçao")
print("Antes de qualquer ca lculo direto dos para metros tem-se que calcular os valores de fase do ensaio a vazio, pois alguns para metros foram dados de linha ou trifasicos. \n")

Vo=Vl/cmath.sqrt(3)
print("Vo = ", Vo.real,"V")

Po= (p-Pva)/3
print("Po = ", Po,"W")

Io = i
print("Io = ", Io,"A")

Rp = Vo.real*Vo.real/Po
print("Rp = ", Rp,"Ohm")

Xm = (Vo.real*Vo.real)/cmath.sqrt((Vo.real*Io)*(Vo.real*Io)-Po*Po)
print("Xm = ", Xm.real,"Ohm")

print("\nDepois de calcular os valores de fase do ensaio a vazio, os valores de fase do ensaio de rotor bloqueado sao calculados. \n")

Vb=Vlblock/cmath.sqrt(3)
print("Vb = ", Vb.real,"V")

Pb= pblock/3
print("Pb = ", Pb,"W")

Ib = iblock
print("Ib = ", Ib,"A")

Re = Pb/(Ib*Ib)
print("Re = ", Re,"Ohm")

R1 = Rblock
print("R1 = ", R1,"Ohm")

R2L = Re-R1
print("R2L = ", R2L,"Ohm")

Xe = cmath.sqrt(((Vb*Ib)*(Vb*Ib))-(Pb*Pb))/(Ib*Ib)
print("Xe = ", Xe.real,"Ohm")

X1 = Xe.real/2
print("X1 = ", X1.real,"Ohm")

print("\n B - O rendimento com escorregamento de 2,5%\n")

s=0.025

V1= Vl/cmath.sqrt(3)
print("V1 = ", V1.real,"V")

print("Zeq")

Zn = Rp*complex(0,Xm)/complex(Rp,Xm)
print("Zn RECTANGULAR = ", Zn)

Ze = R1 + complex(0,X1) + R2L + complex(0,X1) + (1-s)*(R2L/s)
print("Ze RECTANGULAR = ", Ze)

Zeq = (Zn*Ze)/(Zn+Ze)
print("Zeq RECTANGULAR = ", Zeq)

I1 = V1/Zeq
print("I1 = ", I1,"A")

I1p = cmath.polar(I1)
print("I1p = ", I1p)

#P1 = Vo*I1[0]*cmath.cos(I1[1])
#print("P1 = ", P1.real,"W")