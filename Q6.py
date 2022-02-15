import cmath
import math

potencia = 375000
vlinha = 2200
polos =12
freq = 60
#ao girar a vazio com tensão e freq nominais absorve:
current = 20
potency = 14000
#por fase

R1 = 0.4
R2L = 0.2
X1 = 2.0
X2L = X1
escorregamento = 0.02
print("Corrente no estator")

Vf = vlinha/cmath.sqrt(3)
Vf = round(Vf,3)
print("Vf = ", Vf, "V")
