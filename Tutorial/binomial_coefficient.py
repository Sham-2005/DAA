import math
def binomial_coefficient(n,k):
    if n<0 or k<0:
        return "Input must be non negative numbers"
    if k>n:
        return 0
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
n1=int(input("Enter n: "))
k1=int(input("Enter k: "))
print("Binomial Coefficient C({n1},{k1}) is : ", binomial_coefficient(n1,k1))