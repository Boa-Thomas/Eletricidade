import cmath
import math

cv =100
cvconv = 736
t1 =440
t2 = 254
polos = 4
freq = 60
r1 = 0.019
R2L = 0.029
X1 = 0.12
X2L = X1
Rp = 42
Xm = 5.4

print("Considere que o motor é alimentado com tensão de fase igual a 254 V, conexão Y e atinge escorregamento igual a 1,8%")
print("A - Corrente no estator")
s = 0.018

print("R2L_s = ", R2L/s, "Ohm")

print("(1-s)*(R2L_s) = ", (1-s)*(R2L/s), "Ohm")

Z1 = r1+complex(0,X1)
print("Z1 = ", Z1, "Ohm")

Z2 = R2L/s+complex(0,X2L)
print("Z2 = ", Z2, "Ohm")

Zn = Rp*complex(0,Xm)/complex(Rp,Xm)
print("Zn = ", Zn, "Ohm")

Zeq1 = Zn*Z2/(Zn+Z2)
print("Zeq1 = ", Zeq1, "Ohm")

Zeq2 = Z1+Zeq1
print("Zeq2 = ", Zeq2, "Ohm")

I1 = t2/Zeq2
print("I1 = ", I1, "A")

I1p = cmath.polar(I1)

print("B - Fator de pontecia")

FP = cmath.cos(I1p[1])
FPreal = round(FP.real,3)
print("FP = ", FPreal)

print("C - Potencia de entrada")
Pe = t2*I1p[0]*cmath.cos(I1p[1])
pereal = round(Pe.real,3)
print("Pe = ", pereal, "W")

Pe3 = 3*pereal
print("Pe3 = ", Pe3, "W")

print("D - Corrente no rotor")

E1 = t2-Z1*I1
E1p = cmath.polar(E1)
print("E1 = ", E1p, "V")

I2L = E1/Z2
I2Lp = cmath.polar(I2L)
print("I2L = ", I2Lp, "A")

print("E - Potencia na carga")
#professor ultiliza dados polares
Ps = ((R2L*(1-s))/s)*I2Lp[0]*I2Lp[0]
print("Ps = ", Ps, "W")

Ps3 = 3*Ps
print("Ps3 = ", Ps3, "W")

print("F - Velocidade do eixo")
ns = 120*freq/polos
print("ns = ", ns, "rpm")

n = (1-s)*ns
print("n = ", n, "rpm")

w = 2*math.pi*n/60
w = round(w,3)
print("w = ", w, "rad/s")

print("G - Torque na carga")

t = Ps3/w
print("t = ", t, "Nm")

print("H - Rendimento do motor")
eni = Ps3/Pe3*100
print("eni = ", eni, "%")
