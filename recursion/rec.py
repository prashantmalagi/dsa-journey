"""def printnumber(n):
    if n == 5:
        return
    print(n)
    printnumber(n + 1)
printnumber(1)

def print_name(name,n,i):
    # n = int(input("enter n value:"))
    if i == n+1:
        return
    print(name)
    print_name(name, n, i + 1)
print_name("pnm", 8, 0)


class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
"""
class Solution(object):
    def countOdds(self, low, high):
        return (high + 1)//2 - (low - 1)//2
