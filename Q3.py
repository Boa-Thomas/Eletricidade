import cmath
import math

raio = 3
freq = 60
polos = 2
perdarolamento=285
perdanucleo=158
perdarotacional=192
potenciaentreferro=10975
frequenciamotor=1.5

print("A - o escorregamento do rotor")
s = frequenciamotor/freq
print("s = ", s,"%")

print("B - A velocidade sí ncrona e a velocidade do rotor em rpm e em rad/s")
ns = 120*freq/polos
print("ns = ", ns,"rpm")

ws=ns*2*math.pi/60
ws = round(ws,5)
print("ws = ", ws,"rad/s")

n = (1-s)*ns
print("n = ", n,"rpm")

w = 2*math.pi*n/60
w = round(w,5)
print("w = ", w,"rad/s")

print("C - A potencia no eixo do motor (potencia de saída)")
Pd = potenciaentreferro*(1-s)
print("Pd = ", Pd,"W")

Ps = Pd-perdarotacional
print("Ps = ", Ps,"W")

print("D - A eficiencia (rendimento) do motor para as condiçoes apresentadas")
Pe = potenciaentreferro+perdarotacional+perdarolamento
print("Pe = ", Pe,"W")

eni = (Ps/Pe)*100
eni = round(eni,5)
print("eni = ", eni,"%")

print("E - O torque no eixo do motor")
T = 3*Ps/w
T = round(T,5)
print("T = ", T,"N.m")
