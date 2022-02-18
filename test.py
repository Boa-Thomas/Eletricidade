import math
import cmath as cm

zn = complex(12,76)
print(zn)
znp = cm.polar(zn)

print(znp)

print(znp[0],znp[1]*180/math.pi)
