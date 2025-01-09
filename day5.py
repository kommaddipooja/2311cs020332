n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Numbers from 1 to", n, ":")
    for i in range(1, n + 1):
        print(i)

    total = 0
    current = 1
    while current <= n:
        total += current
        current += 1
    
    print("The sum of all numbers from 1 to", n, "is:", total)

def calculate_square(n):
    return n ** 2

number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    result = calculate_square(number)
    print(f"The square of {number} is: {result}")
