import math
import cmath
import numpy


Va = 350000000
t1 = 25000
freq = 60
polos = 4
Xa = 3.25
Ra = 0.25
Carga_3f = 300000000
FP = 0.9

print("\n\nA - Corrente de armadura:\n")
P1f = Carga_3f/3
print("P1f = ", P1f,"W")

S1f = P1f/FP
print("S1f = ", S1f,"VA")

Vt = t1/cmath.sqrt(3)
print("Vt = ", Vt.real,"V")

Ia_mod = S1f/Vt
print("Ia = ", Ia_mod.real,"A")
Ia_ang = cmath.acos(FP)
print("Ia = ", Ia_ang.real,"rad\n",Ia_ang.real*180/math.pi,"°")


print("\n\nB - Tensao Induzida na armadura:\n")

vtp = [Vt.real,0]
Iap = [Ia_mod.real,Ia_ang.real]
comp = cmath.polar(complex(Ra,Xa))[0]
comp2 = cmath.polar(complex(Ra,Xa))[1]
compf = [comp,comp2]
print(compf)
print(Iap)

#ea = numpy.convolve(compf,Iap)+vtp
#print("ea = ", ea,"V")

#Ea = Vt+complex(Ra,Xa)*Ia





