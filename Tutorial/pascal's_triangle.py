def pascal(num_rows):
    if num_rows<=0:
        return []
    triangle=[]
    for i in range(num_rows):
        row=[1]
        if triangle:
            prev_row=triangle[-1]
            for j in range(len(prev_row)-1):
                row.append(prev_row[j]+prev_row[j+1])
            row.append(1)
        triangle.append(row)
    return triangle
def print_pascal(triangle):
    n=len(triangle)
    for i,row in enumerate(triangle):
        row_str=' '.join(map(str,row))
        print(row_str.center(n*3))
result=pascal(5)
print_pascal(result)