import cmath
import math


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
Voreal = round(Vo.real,3)
print("Vo = ", Voreal,"V")


Po= (p-Pva)/3
print("Po = ", Po,"W")

Io = i
print("Io = ", Io,"A")

Rp = Voreal*Voreal/Po
Rp = round(Rp,3)
print("Rp = ", Rp,"Ohm")

Xm = (Voreal*Voreal)/cmath.sqrt((Voreal*Io)*(Voreal*Io)-Po*Po)
Xmreal = round(Xm.real,3)
print("Xm = ", Xmreal,"Ohm")

print("\nDepois de calcular os valores de fase do ensaio a vazio, os valores de fase do ensaio de rotor bloqueado sao calculados. \n")

Vb=Vlblock/cmath.sqrt(3)
Vbreal = round(Vb.real,3)
print("Vb = ", Vbreal,"V")

Pb= pblock/3
Pb = round(Pb,3)
print("Pb = ", Pb,"W")

Ib = iblock
Ib = round(Ib,3)
print("Ib = ", Ib,"A")

Re = Pb/(Ib*Ib)
Re = round(Re,3)
print("Re = ", Re,"Ohm")

R1 = Rblock
R1 = round(R1,3)
print("R1 = ", R1,"Ohm")

R2L = Re-R1
R2L = round(R2L,3)
print("R2L = ", R2L,"Ohm")

Xe = cmath.sqrt(((Vb*Ib)*(Vb*Ib))-(Pb*Pb))/(Ib*Ib)
Xereal = round(Xe.real,3)
print("Xe = ", Xereal,"Ohm")

X1 = Xereal/2
X1 = round(X1,3)
print("X1 = ", X1,"Ohm")

print("\n B - O rendimento com escorregamento de 2,5%\n")

s=0.025

V1= Vl/cmath.sqrt(3)
V1real = round(V1.real,3)
print("V1 = ", V1real,"V")

Zn = Rp*complex(0,Xm)/complex(Rp,Xm)
Znaux1 = round(Zn.real,4)
Znaux2 = round(Zn.imag,4)
Zn = complex(Znaux1,Znaux2)
print("Zn RECTANGULAR = ", Zn)


Ze = R1 + complex(0,X1) + R2L + complex(0,X1) + (1-s)*(R2L/s)
print("Ze RECTANGULAR = ", Ze)

Zeq = (Zn*Ze)/(Zn+Ze)
Zeqaux1 = round(Zeq.real,4)
Zeqaux2 = round(Zeq.imag,4)
Zeq = complex(Zeqaux1,Zeqaux2)
print("Zeq RECTANGULAR = ", Zeq)

I1 = V1/Zeq
I1aux1 = round(I1.real,3)
I1aux2 = round(I1.imag,3)
I1 = complex(I1aux1,I1aux2)
print("I1 = ", I1,"A")

I1p = cmath.polar(I1)
print("I1p = ", I1p)

P1 = Vo*I1p[0]*cmath.cos(I1p[1])
P1aux1 = round(P1.real,3)
P1aux2 = round(P1.imag,3)
P1 = complex(P1aux1,P1aux2)
print("P1 = ", P1.real,"W")

If = V1real/Zn
Ifaux1 = round(If.real,3)
Ifaux2 = round(If.imag,3)
If = complex(Ifaux1,Ifaux2)
print("If = ", If,"A")

I2 = V1real/Ze
I2aux1 = round(I2.real,3)
I2aux2 = round(I2.imag,3)
I2 = complex(I2aux1,I2aux2)
print("I2 = ", I2,"A")

P2 = (1-s)*(R2L/s)*I2.real*I2.real
P2aux1 = round(P2.real,3)
P2aux2 = round(P2.imag,3)
P2 = complex(P2aux1,P2aux2)
print("P2 = ", P2.real,"W")

eni = (P2.real/P1.real)*100
eni = round(eni,3)
print("eni = ", eni,"%")

print("\n B - O torque nesta condiçao\n")
print("A velocidade síncrona e a rotaçao do motor sao calculadas por:")

ns = 120*freq/polos
print("ns = ", ns,"rpm")

n = (1-s)*ns
print("n = ", n,"rpm")

print("\nA velocidade angular do motor sera :")
w = 2*math.pi*n/60
w = round(w,3)
print("w = ", w,"rad/s")

T = 3*P2.real/w
T = round(T,3)
print("T = ", T,"N.m")
