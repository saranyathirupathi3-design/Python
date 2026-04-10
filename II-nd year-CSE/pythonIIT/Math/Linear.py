def solve_2eq_3var():
    print("Solve: a1x + b1y + c1z = d1")
    print("       a2x + b2y + c2z = d2")
    print("Enter coefficients (if a variable isn't present, enter 0)\n")

    try:
        
        a1 = float(input("Eq1 - a1 (x): "))
        b1 = float(input("Eq1 - b1 (y): "))
        c1 = float(input("Eq1 - c1 (z): "))
        d1 = float(input("Eq1 - d1 (constant): "))

        
        a2 = float(input("Eq2 - a2 (x): "))
        b2 = float(input("Eq2 - b2 (y): "))
        c2 = float(input("Eq2 - c2 (z): "))
        d2 = float(input("Eq2 - d2 (constant): "))

        
        matrix = [
            [a1, b1, c1, d1],
            [a2, b2, c2, d2]
        ]


        
        if matrix[0][0] == 0:
            matrix[0], matrix[1] = matrix[1], matrix[0]
        
        
        if matrix[0][0] != 0:
            
            factor = matrix[1][0] / matrix[0][0]
            for j in range(4):
                matrix[1][j] -= factor * matrix[0][j]

        
        z = 0.0
        
        if matrix[1][1] != 0:
            y = (matrix[1][3] - (matrix[1][2] * z)) / matrix[1][1]
            x = (matrix[0][3] - (matrix[0][2] * z) - (matrix[0][1] * y)) / matrix[0][0]
            print(f"\nSolution (assuming z=0):")
            print(f"x = {x:.4f}")
            print(f"y = {y:.4f}")
            print(f"z = {z:.4f} (Free Variable)")
        else:
            print("\nSystem has no unique solution or is dependent.")

    except ZeroDivisionError:
        print("\nError: Division by zero. The equations might be parallel or invalid.")
    except ValueError:
        print("\nError: Please enter valid numerical values.")


solve_2eq_3var()
