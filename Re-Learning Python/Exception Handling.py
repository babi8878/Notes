# Example of exception handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print("This will always execute.")
