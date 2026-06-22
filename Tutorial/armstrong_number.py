def armstrong(n):
    num_str=str(n)
    power=len(num_str)
    total_sum=0
    for i in num_str:
        total_sum=total_sum+int(i)**power
    return total_sum==n
print(armstrong(154))