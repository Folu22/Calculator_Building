def addition(a,b):
    """Returns the sum of a and b."""
    sum = a + b
    return sum

def subtracttion(a, b):
    """Returns the difference of a and b."""
    subtract = a - b
    return subtract

def multiplication(a, b):
    """Returns the product of a and b."""
    product = a * b
    return product

def division(a, b):
    """Returns the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    quotient = a / b
    return quotient

def main():
    while True:
        try:
            choice = input("Choose an operation: +, -, *, / or 'exit' to quit: ")
            if choice == 'exit':
                break
            first_num = int(input("Enter first number: "))
            second_num = float(input("Enter second number: "))
            
            if choice == '+':
                print(f"Result: {addition(first_num, second_num)}")
            elif choice == '-':
                print(f"Result: {subtracttion(first_num, second_num)}")
            elif choice == '*':
                print(f"Result: {multiplication(first_num, second_num)}")
            elif choice == '/':
                print(f"Result: {division(first_num, second_num)}")
            else:
                print("Invalid operation. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()