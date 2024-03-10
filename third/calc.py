def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "(Error) Division by zero"
    return num1 / num2

while True:
    print("Calculator Menu:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
      print("Exiting the calculator. Goodbye!")
      break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid input. Please choose a valid option.")
        input("Press Enter to continue...")
        continue

    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter numeric values.")
      input("Press Enter to continue...")
      continue

    if choice == '1':
      result = addition(num1, num2)
      print(f"Addition Result: {result}")
    elif choice == '2':
      result = subtraction(num1, num2)
      print(f"Subtraction Result: {result}")
    elif choice == '3':
      result = multiplication(num1, num2)
      print(f"Multiplication Result: {result}")
    elif choice == '4':
      result = division(num1, num2)
      print(f"Division Result: {result}")
        
    input("Press Enter to continue...")