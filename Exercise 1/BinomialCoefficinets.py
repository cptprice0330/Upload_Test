import matplotlib

import commonLib

x = commonLib.Binomial(8,5)
print(x)


y = []
for i in range (1,20):
    for j in range(0,i):
        y.append(commonLib.Binomial(i,j))
    print(y)


