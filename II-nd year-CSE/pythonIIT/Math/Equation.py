print("=== Simple Math Operations ===")
num = float(input("Enter a number: "))
square = num * num           # x^2
cube = num * num * num       # x^3
square_root = num ** 0.5     # sqrt(x)
inverse = 1 / num            # 1/x
print("\nMath results:")
print("Square:", square)
print("Cube:", cube)
print("Square root:", round(square_root, 3))
print("Inverse:", round(inverse, 3))
print("\n Solve Two Linear Equations ")
print("Equations of the form: a1*x + b1*y = c1  and  a2*x + b2*y = c2")
a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))

a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))
if a1 != 0:
    numerator = c2 - (a2 * c1 / a1)
    denominator = b2 - (a2 * b1 / a1)
    
    if denominator != 0:
        y = numerator / denominator
        x = (c1 - b1 * y) / a1
        print("\nSolution of the equations:")
        print("x =", round(x, 3))
        print("y =", round(y, 3))
    else:
        print("No unique solution exists (denominator is zero)")
else:
    print("Cannot solve using substitution because a1 is zero")
