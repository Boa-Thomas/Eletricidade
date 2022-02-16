import cmath
import math

hp = 0.25
hp_to_w = 746*hp
t1 = 110
polos = 4
freq = 60
r1 = 2.02
r2 = 4.12
x1 = 2.79
x2 = 2.12
xm = 66.8
# rp negligenciado
s = 0.05
perdas_nucleo = 24
perdas_vestilacao_atrito = 13

print("A - Corrente no Estator")

z1 = complex(r1, x1)
print("z1 = ", z1,"Ohms")

aux = (0.5 * (r2/s)) + (complex(0,0.5) * x2)
zd = complex(0,0.5)*xm*(aux) / (complex(0,0.5)*xm + aux)
print("zd = ", zd,"Ohms")

zo = complex(0,0.5*xm)*complex((0.5*r2)/(2-s),0.5*x2)/(complex(0,0.5*xm)+complex((0.5*r2)/(2-s),0.5*x2))
print("zo = ", zo,"Ohms")

zeq = z1+zd+zo
print("zeq = ", zeq,"Ohms")

I1 = t1/zeq
print("I1 = ", I1,"A")

I1p = cmath.polar(I1)
print("B - Fator de potencia")

FP = cmath.cos(I1p[1])
FPreal = round(FP.real,3)
print("FP = ", FPreal)

print("C - Potencia de entrada")
P1 = t1*I1p[0]*FPreal
print("P1 = ", P1,"W")

print("D - Potencia de saída")

I2d = I1*((complex(0,0.5)*xm)/(complex(0,0.5*xm)+(0.5*(r2/s)+complex(0,0.5)*x2)))
print("I2d = ", I2d,"A")

I2o = I1*((complex(0,0.5*xm)/(complex(0,0.5*xm)+(0.5*r2/(2-s)+complex(0,0.5)*x2))))
print("I2o = ", I2o,"A")

Pcd = (0.5*r2*(1-s)/s)*cmath.polar(I2d)[0]*cmath.polar(I2d)[0]
print("Pcd = ", Pcd,"W")

Pco = (0.5*r2*(1-s)/(2-s))*cmath.polar(I2o)[0]*cmath.polar(I2o)[0]
Pco = -Pco
print("A potencia em oposiça o e negativa em virtude de o campo ser em oposiça o ao campo direto")
Pco = round(Pco,4)
print("Pco = ", Pco,"W")

Pc = Pcd + Pco
Pc = round(Pc,4)
print("Pc = ", Pc,"W")

P2 = Pc -perdas_nucleo -perdas_vestilacao_atrito
P2 = round(P2,4)
print("P2 = ", P2,"W")

P2h = P2/746
P2h = round(P2h,4)
print("P2 = ", P2h,"hp")

print("E - Rendimento")
eni = P2/P1*100
eni = round(eni,4)
print("eni = ", eni,"%")

print("F - Velocidade no eixo")
ns = 120*freq/polos
print("ns = ", ns,"rpm")

ws = ns*2*math.pi/60
print("ws = ", ws,"rad/s")

n = (1-s)*ns
print("n = ", n,"rpm")

w = ws*(1-s)
print("w = ", w,"rad/s")

print("G - Torque na carga")
t = P2/w
t = round(t,4)
print("t = ", t,"Nm")
