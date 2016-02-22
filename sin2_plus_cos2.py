#a
from math import sin,cos,pi

x = pi/4
val1 = sin(x)**2 + cos(x)**2
print val1

#b compute
v0 = 3
t = 1
a = 2**2
s = v0*t + 0,5*1*2**2
print s

#c verify these equations
#(a+b)**2 = a**2 + 2ab+b**2
#(a-b)**2 = a**2 - 2ab+b**2
a = 3.3
b = 5.3
a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print "First equation: %f = %f" % (eq1_sum, eq1_pow)
print "Seconds equation: %f = %f" % (eq2_pow, eq2_pow)
