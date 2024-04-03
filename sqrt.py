#SQRT by Newtons algo
import math
x=int(input("Ënter the number:"))
z=1
while (True):
    root=(z+x/z)/2
    if (abs(root-z)<1):
        break
    z=root
print('Root=',root)
print("Python's estimate:",math.sqrt(x))
