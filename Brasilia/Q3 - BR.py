import cmath
import math

raio = 3
freq = 60
polos = 4
perdarolamento=545
perdanucleo=308
perdarotacional=112
perda_barra = 244
potenciaentreferro=21975
frequenciamotor=1.8

print("\nA - o escorregamento do rotor\n")
s = frequenciamotor/freq
print("s = ", s,"%")

print("\nB - A velocidade sí ncrona e a velocidade do rotor em rpm e em rad/s\n")
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

print("\nC - A potencia no eixo do motor (potencia de saída)\n")
Pd = potenciaentreferro*(1-s)
print("Pd = ", Pd,"W")

Ps = Pd-perdarotacional
print("Ps = ", Ps,"W")

print("\nD - A eficiencia (rendimento) do motor para as condiçoes apresentadas\n")
Pe = potenciaentreferro+perdarotacional+perdarolamento+perda_barra
print("Pe = ", Pe,"W")

eni = (Ps/Pe)*100
eni = round(eni,5)
print("eni = ", eni,"%")

print("\nE - O torque no eixo do motor\n")
T = 3*Ps/w
T = round(T,5)
print("T = ", T,"N.m")
