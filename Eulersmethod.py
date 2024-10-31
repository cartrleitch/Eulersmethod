import math

fancy = input("More complex form of Euler's method? Y/N: ").upper()
h = float(input("Enter h: "))
y0 = float(input("Enter y0: "))
y1tofind = float(input("Enter x1 value to find y of: "))

xarr = [] 
yarr = []
yarr.append(y0)
xarr.append(0)

# Derivative equation
def yder(x, y):
    return (2*y + x)

print(f"\nNumber of iterations: {round(y1tofind/h)}\n")
for n in range(1, (round(float(y1tofind/h))+1)):
    print(f"Iterations: {n}")
    xarr.append(h*n)
    if (fancy == "Y"):
        yarr.append(yarr[n-1] + h * (((yder(h*(n-1), yarr[n-1])) + yder(h*n, (yarr[n-1]+ h*yder(h*(n-1), yarr[n-1]))))/2))
    else:
        yarr.append(yarr[n-1] + h * yder(h*(n-1), yarr[n-1]))

print(f"\nAnswer: {yarr[len(yarr)-1]}")
