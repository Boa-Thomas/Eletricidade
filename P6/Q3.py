import math
import cmath

#gerador
potencia = 800000
#rotor cilindrico
T_linha = 11000
#estrela
R_armadura = 1.5
Reatancia_sync = 25 #por fase
carga = 600000
FP = 0.8

print("\n\nA - Regulação de tensão percentual:\n")

vt = T_linha/cmath.sqrt(3)
print("Vt",vt.real,"V")

ang = cmath.acos(FP)
print("ang",ang.real*180/cmath.pi,"rad")

Ia = (carga/3)/vt.real
print("Ia",Ia.real,"A")

Ia_rect = cmath.rect(Ia.real, ang.real)
print("Ia_rect",Ia_rect,"A")
Vt_Rect = cmath.rect(vt.real, 0)
print("Vt_rect",Vt_Rect,"V")


Ea = Vt_Rect + (complex(R_armadura,Reatancia_sync)*Ia_rect)
Ea_p = cmath.polar(Ea)
print("Ea",Ea_p,"V")

R_por = ((Ea_p[0]-vt.real)/vt.real)*100
print("R%",R_por,"%")

print("\n\nB - Angulo de carga:\n")
print("§",Ea_p[1]*180/cmath.pi,"°")


print("\n\nC - A pote ncia trifa sica desenvolvida pelo gerador em watts:\n")
##
pd = ((Ea[0]*vt.real)/Reatancia_sync)*|-1|
print("pd",pd,"W")