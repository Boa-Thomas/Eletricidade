import math
import cmath
import numpy


Va = 50000000
t1 = 3200
freq = 60
polos = 14
Xa = 1.5
Ra = 0.25
Carga_3f = 30000000
FP = 0.85

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

Ia_Rect =cmath.rect(Ia_mod.real, -Ia_ang.real)
print("Ia_rect = ", Ia_Rect,"A")
Vt_Rect = cmath.rect(Vt.real, 0)
print("Vt_rect = ", Vt_Rect,"V")


Ea = Vt_Rect + (complex(Ra,Xa)*Ia_Rect)
Eap = cmath.polar(Ea)
print("Ea = ", Eap,"V")

print("\n\nC - Ângulo da carga:\n")

print("§ = ", Eap[1]*180/math.pi,"°")

print("\n\nD - Regulação de tensão percentual:\n")

R_por = ((Eap[0]-Vt.real)/Vt.real)*100
print("R% = ", R_por,"%")

print("\n\nE - Velocidade no eixo do gerador:\n")

ns = 120*freq/polos
print("ns = ", ns,"RPM!!!!!!!!!!!!!!!!!!!!")

ws = 2*math.pi*ns/60
print("ws = ", ws,"rad/s")



