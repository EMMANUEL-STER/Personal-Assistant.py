import math

def add(*args):
    """Return the sum of all numbers."""
    return sum(args)

def subtract(*args):
    """Subtract all subsequent numbers from the first."""
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    """Multiply all numbers together."""
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    """Divide the first number by all subsequent numbers."""
    if not args:
        return None
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error! Division by zero."
        result /= num
    return result

def power(base, exp):
    """Raise base to the power of exp."""
    return math.pow(base, exp)

def square_root(x):
    """Return the square root of x."""
    if x < 0:
        return "Error! Cannot take square root of a negative number."
    return math.sqrt(x)

print("=== Variadic Calculator ===")
print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")

choice = input("Enter choice (1/2/3/4/5/6): ")

if choice in ['1', '2', '3', '4']:
    nums = tuple(map(float, input("Enter numbers separated by spaces: ").split()))
    if choice == '1':
        print("Result:", add(*nums))
    elif choice == '2':
        print("Result:", subtract(*nums))
    elif choice == '3':
        print("Result:", multiply(*nums))
    elif choice == '4':
        print("Result:", divide(*nums))

elif choice == '5':
    base = float(input("Enter base: "))
    exp = float(input("Enter exponent: "))
    print("Result:", power(base, exp))

elif choice == '6':
    num = float(input("Enter number: "))
    print("Result:", square_root(num))

else:
    print("Invalid choice!")