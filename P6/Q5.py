import math
import cmath

potencia = 200000
t1 = 2200
#estrela
FP = 0.8
Xd = 4
Xq = Xd/2
print("\n\nA - Angulo de carga:\n")
vt = t1/cmath.sqrt(3)
print ("vt = ", vt.real,"V")

Ia = (potencia/3)/vt
print ("Ia = ", Ia.real,"A")

ang = math.acos(FP)
print ("ang = ", ang,"rad")
seno = math.sin(ang)
print ("seno = ", seno)

tan = (Ia*Xq*FP)/(vt+Ia*Xq*seno)
print ("tan de 'SIGMA' = ", tan.real,"rad")

sigma = math.atan(tan.real)
print ("'SIGMA' = ", sigma,"rad")

print("\n\nB - A regulaçao de tensao percentual:\n")

Ea = vt*math.cos(sigma) + Ia*Xd*math.sin(sigma+ang)
print ("Ea = ", Ea.real,"V")

R_por = ((Ea.real-vt.real)/vt.real)*100
print ("R% = ", R_por,"%")

print("\n\nC - A potencia desenvolvida pelo gerador:\n")

pd= (((Ea.real*vt.real)/Xd)*math.sin(sigma))+((vt.real*vt.real)/2)*((1/Xq)-(1/Xd))*math.sin(2*sigma)
print ("Pd = ", pd.real,"W")

pd3 = pd.real*3
print ("Pd trifasico = ", pd3,"W")

print("\n\nD - Qual a parcela desenvolvida pela salida ncia do rotor:\n")
pq = ((vt.real*vt.real)/2)*((1/Xq)-(1/Xd))*math.sin(2*sigma)
print ("pq = ", pq.real,"W")
pq3 = pq.real*3
print ("pq trifasico = ", pq3,"W\n\n")