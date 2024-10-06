# def fibonacci(n):
#     fib_series = []
#     if n <= 0:
#         return "Please enter a positive integer."
#     elif n == 1:
#         fib_series.append(0)
#     elif n == 2:
#         fib_series.extend([0, 1])
#     else:
#         fib_series.extend([0, 1])
#         for i in range(2, n):
#             fib_series.append(fib_series[-1] + fib_series[-2])
#     return fib_series
# n = int(input("Enter the length of Fibonacci series : "))
# fib = fibonacci(n)
# print(fib)
# # for num in fib:
# # 	print(f"{num}")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

    next_calculation = input("Do you want to perform another calculation? (y/n): ")
    if next_calculation.lower() != 'y':
        break
