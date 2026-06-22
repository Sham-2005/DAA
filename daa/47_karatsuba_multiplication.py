def karatsuba(x, y):
    if x < 10 or y < 10: return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    high_x, low_x = divmod(x, 10**half)
    high_y, low_y = divmod(y, 10**half)
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)
    return (z2 * 10**(2*half)) + ((z1 - z2 - z0) * 10**half) + z0
print(karatsuba(1234, 5678)) 