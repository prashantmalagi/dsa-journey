"""Right-angled triangle pattern of stars in ascending and descending order."""
n=int(input("Enter a number: "))
for i in range(1, n + 1):
    print("" * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()

n = int(input("Enter a number: "))
for i in range(n,0,-1):
    print("" * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()
