# --coding utf-8--
import os
import math

os.system("cls")
print("Input coefficients of square equation")
a = float(input())
b = float(input())
c = float(input())
print(f"try to solve equation:{a}*x^2+{b}*x+{c}=0")
if ((a == 0) and (b == 0)) and (c == 0):
    print("The answer is any number")
elif (a == 0) and (b != 0) and (c != 0):
    print(f"The equation has the following solution:{-b / a}")
elif (a == 0) and (b == 0) and (c != 0):
    print("The equation has no roots")
else:
    d = b * b - 4 * a * c
    sign = (d > 0) - (d < 0)
    nRoots = sign + 1
    if nRoots > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print("The equation has the following roots:")
        print("x1 = " + x1)
        print("x2 = " + x2)
    else:
        print("The equation has no roots")