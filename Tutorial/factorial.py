def fact(n):
    if n<0:
        return "Factorial is not defined for negative numbers"
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))