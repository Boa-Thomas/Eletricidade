import math
import cmath
from tkinter import END


Va = 350000000
t1 = 25000
freq = 60
polos = 4
Xa = 3.25
Ra = 0.25
Carga_3f = 300000000
FP = 0.9

print("\n\nA - Corrente de armadura:\n")
P1f = Carga_3f/3
print("P1f = ", P1f,"W")

S1f = P1f/FP
print("S1f = ", S1f,"VA")

Vtp = t1/cmath.sqrt(3)
print("Vt = ", Vtp,"V")

Ia = S1f/Vtp
print("Ia = ", Ia,"A")

Ia_polar = [Ia.real,cmath.acos(FP)]
