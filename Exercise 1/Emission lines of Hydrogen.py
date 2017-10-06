import scipy.constants
import commonLib


R = 1.097e-2

for m in range (1,5):
    print("m: ",m)
    for n in range (m+1,m+6):
        lambdaVI = R*((1/m**2) - (1/n**2))
        print(1/lambdaVI)


