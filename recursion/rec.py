"""def printnumber(n):
    if n == 5:
        return
    print(n)
    printnumber(n + 1)
printnumber(1)
"""
def print_name(name,n,i):
    # n = int(input("enter n value:"))
    if i == n+1:
        return
    print(name)
    print_name(name, n, i + 1)
print_name("sai", 8, 0)

    