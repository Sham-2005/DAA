def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
num=int(input("Enter a number to reverse: "))
print("Reversed Number is:", reverse(num))