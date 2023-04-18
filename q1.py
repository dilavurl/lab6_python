
n = int(input("Enter n: "))
x = int(input("Enter x: "))

factorial = lambda num: 1 if num == 0 else num * factorial(num - 1)

term = lambda i: n**i / factorial(i)

series = [term(i) for i in range(x+1)]

result = sum(series)

result += 1

print(f"The value of e^n is: {result}")