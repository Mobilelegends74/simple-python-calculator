# calculator/main.py
from calculator.operations import add, subtract, multiply, divide

def main():
    print("Welcome to the Python Calculator!")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    try:
        print(f"Division: {divide(a, b)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
