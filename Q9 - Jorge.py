import cmath
import math

#motor trifasico
polos = 12
freq = 60
s = 0.025
torque_eletro= 500
rpm = 480
reatancia_de_dispersao = 3

ns = 120*freq/polos
print("ns = ", ns, "rpm")

s_ast=(ns-rpm)/ns
print("s_ast = ", s_ast)

T = ((2*(s_ast/s))/((1+(s_ast/s)*(s_ast/s)))*torque_eletro)
T = round(T,3)
print("T = ", T, "Nm")

