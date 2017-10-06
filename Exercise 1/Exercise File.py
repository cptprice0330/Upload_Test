import scipy
import scipy.constants
import math

g = scipy.constants.g
G = scipy.constants.G
valid = False

#

s = float(input("Enter the height that the ball is dropped from in m: "))
while not valid:
    if s < 0:
        s = float(input("You're not dropping the ball up; enter a height in m: "))
    else:
        valid = True

valid = False
m = float(input("Enter the mass of the ball in Kg: "))
while not valid:
    if m < 0:
        m = float(input("Negative mass? Are you insane? Enter mass in Kg: "))
    if m > 60:
        m = float(input("A little on the heavy side for a ball Enter mass in Kg: "))
    else:
        valid = True

#

t = 2*s
t = t/g
t = math.sqrt(t)

v = g*t

gpe = m*g*s
Ek = (1/2)*m*v**2

print("The ball of mass: ",m,"kg was dropped from height: ",s,"m;")
print("Time taken  for it to drop: ",t,"s")
print("GPE gained : ",gpe,"J")
print("Kinetic energy gained: ",Ek,"J")
