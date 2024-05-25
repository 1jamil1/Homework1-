def factorial(n):
    if n == 0:
        return 1
    elif n<0:
        return "Undefined"
    else:
        a=1
        while n>0:
            a=a*n
            n=n-1
        return a

number = int(input("Enter a number: "))
result = factorial(number)
print(result)