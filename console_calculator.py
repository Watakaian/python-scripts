import math

print("=" * 40)
print("SCIENTIFIC CALCULATOR")
print("=" * 40)

def show_menu():
    print("\nChoose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Sine (degrees)")
    print("9. Cosine (degrees)")
    print("10. Tangent (degrees)")
    print("11. Logarithm (base 10)")
    print("12. Natural Log (ln)")
    print("13. Absolute Value")
    print("0. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Please enter a valid number")

def get_integer(prompt):
    while True:
        try:
            return int(float(input(prompt)))
        except:
            print("Please enter a valid whole number")

# calculator loop
while True:
    show_menu()
    
    choice = input("\nEnter your choice (0-13): ")
    
    if choice == "0":
        print("\nGoodbye")
        break
    
    elif choice == "1":  # add
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    
    elif choice == "2":  # subtract
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    
    elif choice == "3":  # multiply
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        result = num1 * num2
        print(f"Result: {num1} × {num2} = {result}")
    
    elif choice == "4":  # divide
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            result = num1 / num2
            print(f"Result: {num1} ÷ {num2} = {result}")
    
    elif choice == "5":  # power
        base = get_number("Enter base number: ")
        exponent = get_number("Enter exponent: ")
        result = base ** exponent
        print(f"Result: {base}^{exponent} = {result}")
    
    elif choice == "6":  # square Root
        num = get_number("Enter a number: ")
        if num < 0:
            print("Error: Cannot find square root of negative number")
        else:
            result = math.sqrt(num)
            print(f"Result: sqrt({num}) = {result}")
    
    elif choice == "7":  # factorial
        num = get_integer("Enter a whole number: ")
        if num < 0:
            print("Error: Cannot find factorial of negative number")
        else:
            result = math.factorial(num)
            print(f"Result: {num}! = {result}")
    
    elif choice == "8":  # sine
        angle = get_number("Enter angle in degrees: ")
        radians = math.radians(angle)
        result = math.sin(radians)
        print(f"Result: sin({angle}°) = {result}")
    
    elif choice == "9":  # cosine
        angle = get_number("Enter angle in degrees: ")
        radians = math.radians(angle)
        result = math.cos(radians)
        print(f"Result: cos({angle}°) = {result}")
    
    elif choice == "10":  # tangent
        angle = get_number("Enter angle in degrees: ")
        radians = math.radians(angle)
        result = math.tan(radians)
        print(f"Result: tan({angle}°) = {result}")
    
    elif choice == "11":  # logarithm
        num = get_number("Enter a positive number: ")
        if num <= 0:
            print("Error: Number must be positive")
        else:
            result = math.log10(num)
            print(f"Result: log({num}) = {result}")
    
    elif choice == "12":  # natural Log
        num = get_number("Enter a positive number: ")
        if num <= 0:
            print("Error: Number must be positive")
        else:
            result = math.log(num)
            print(f"Result: ln({num}) = {result}")
    
    elif choice == "13":  # absolute Value
        num = get_number("Enter a number: ")
        result = abs(num)
        print(f"Result: |{num}| = {result}")
    
    else:
        print("Invalid choice! Please try again.")
    
    print("-" * 40)
