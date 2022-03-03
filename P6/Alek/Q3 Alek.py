import math
import cmath

#gerador
potencia = 15000
#rotor cilindrico
T_linha = 220
#estrela
R_armadura = 0.12
Reatancia_sync = 1.25 #por fase
carga = 15000
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


print("\n\nC - A potencia trifasica desenvolvida pelo gerador em watts:\n")
pd = ((Ea_p[0]*vt.real)/Reatancia_sync)*cmath.sqrt((cmath.sin(Ea_p[1]))*(cmath.sin(Ea_p[1])))
print("pd por fase",pd.real,"W")
print("pd trifasico",pd.real*3,"W")
print("\nFormula alternativa\n")
pd = vt.real*Ia.real*FP
print("pd por fase",pd.real,"W")

