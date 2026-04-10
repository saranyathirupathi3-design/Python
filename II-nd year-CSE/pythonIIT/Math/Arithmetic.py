def perform_operations():
   
   

    # --- 1. Arithmetic Operations ---
    print("\n--- Arithmetic Operations (on two numbers) ---")
    try:
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print(f"\nResults for {num1} and {num2}:")
       
        print(f"1. Addition (+): {num1 + num2}")
        print(f"2. Subtraction (-): {num1 - num2}")
        print(f"3. Multiplication (*): {num1 * num2}")
        print(f"4. Division (/): {num1 / num2}")
        print(f"5. Floor Division (//): {num1 // num2}")
        print(f"6. Modulus (%): {num1 % num2}")
        print(f"7. Exponentiation (**): {num1 ** num2}")
        
    except ValueError:
        print("Invalid input for numbers. Please enter numerical values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed for division, floor division, or modulus.")

    
    print("\n--- Set Operations (on two sets of colors) ---")
    try:
        
        set_a = {"red", "green", "blue", "yellow"}
        set_b = {"blue", "purple", "red", "orange"}
        print(f"Set A: {set_a}")
        print(f"Set B: {set_b}")

        
        print("\nSet Operation Results:")
        print(f"1. Union (A | B): {set_a | set_b}") # Combines all unique elements
        print(f"2. Intersection (A & B): {set_a & set_b}") # Common elements
        print(f"3. Difference (A - B): {set_a - set_b}") # Elements in A but not in B
        print(f"4. Symmetric Difference (A ^ B): {set_a ^ set_b}") # Elements in either A or B, but not both

    except Exception as e:
        print(f"An error occurred during set operations: {e}")

    

if __name__ == "__main__":
    perform_operations()
