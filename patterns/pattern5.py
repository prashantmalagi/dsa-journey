n=int(input("Enter the number of rows: "))
for i in range(n):
    # Print spaces
    print(" " * (n - i - 1), end="")

    for j in range(2 * i + 1):
        print("*", end="")

    print()