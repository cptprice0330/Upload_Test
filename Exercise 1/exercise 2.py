#import scipy
import scipy.constants
import math
import commonLib



time = [0,0,440,0,0]

t = float(input("Enter a time in seconds: "))

commonLib.timeConverter(time)

commonLib.twoNumberInsideInputValidate(0,100000,t)

time[0] = math.floor(time[0])
print(time)
R = 6371000
M = 5.79*(10**24)

h = (scipy.constants.G * M * (t ** 2) / (4 * (math.pi ** 2))) ** (1 / 3)
h = h-R

print(h)

