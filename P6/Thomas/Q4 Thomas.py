import math
import cmath

from numpy import mat

#gerador
#sincrono
#trifasico
potencia = 21000
t1 = 380
#Estrela
FP = 0.95
Xd = 4
Xq = Xd/2

print("\n\nA - Angulo de carga:\n")

Vt = t1/cmath.sqrt(3)
print("Vt",Vt.real,"V")

Ia = (potencia/3)/(Vt.real)
print("Ia",Ia.real,"A")

ang = cmath.acos(FP)
print("ang",ang.real*180/cmath.pi,"°")
seno = cmath.sin(ang.real)
print("seno de",ang.real*180/cmath.pi," = ",seno.real)

tan = (Ia.real * Xq * FP)/(Vt.real + (Ia.real * Xq*seno))
print("tan de (§): ", tan.real)

sig = cmath.atan(tan.real)
print("§ de (tan): ", sig.real*180/cmath.pi,"°")

print("\n\nB - A regulaça o de tensa o percentual:\n")

Ea = Vt*math.cos(sig.real) + Ia*Xd*math.sin(sig.real+ang.real)
print("Ea",Ea.real,"V")

R_por = ((Ea.real-Vt.real)/Vt.real)*100
print("R%",R_por,"%")

print("\n\nC - A pote ncia desenvolvida pelo gerador:\n")

Pd = (((Ea.real*Vt.real)/Xd)*cmath.sin(sig.real))+((Vt.real*Vt.real)/2)*((1/Xq)-(1/Xd))*math.sin(2*sig.real)
print("Pd",Pd.real,"W")

pd3 = Pd.real*3
print("Pd trifasico",pd3,"W")

print("\n\nD - Qual a parcela desenvolvida pela salie ncia do rotor:\n")
pq = ((Vt.real*Vt.real)/2)*((1/Xq)-(1/Xd))*math.sin(2*sig.real)
print("pq",pq.real,"W")
pq3 = pq.real*3
print("pq trifasico",pq3,"W")
