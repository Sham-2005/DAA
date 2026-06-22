def assembly_line_scheduling(n, a1, a2, t1, t2, e1, e2, x1, x2):
    T1 = [0] * n
    T2 = [0] * n
    T1[0] = e1 + a1[0]
    T2[0] = e2 + a2[0]
    for i in range(1, n):
        T1[i] = min(T1[i-1] + a1[i], T2[i-1] + t2[i-1] + a1[i])
        T2[i] = min(T2[i-1] + a2[i], T1[i-1] + t1[i-1] + a2[i])
    return min(T1[n-1] + x1, T2[n-1] + x2)
n = 4
a1 = [4, 5, 3, 2]
a2 = [2, 10, 1, 4]
t1 = [0, 7, 4, 5] 
t2 = [0, 9, 2, 8]
e1, e2 = 10, 12
x1, x2 = 18, 7