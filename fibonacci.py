# Non-Recursive Fibonacci Function
def non_recursive(n):
    a = 0
    b = 1

    print("Non-Recursive Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")

        c = a + b
        a = b
        b = c

    print()

# Recursive Fibonacci Function
def recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive(n - 1) + recursive(n - 2)


# Main Program
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Enter a positive number")
else:
    non_recursive(n)

    print("Recursive Fibonacci Series:")

    for i in range(n):
        print(recursive(i), end=" ")

    print()
