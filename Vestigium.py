def trace(x):
    diag = [x[i][i] for i in range(len(x))]
    sum_diag=sum(diag)
    return sum_diag

def row_check(x):
    x_sorted = qsort(x)
    if x_sorted == list(range(1,len(x_sorted)+1)):
        return True
    else:
        return False

def matrix_check(matrix):
    rows_duplicated = []
    i=0
    for row in matrix:
        if row_check(row)==False:
            i+=1
    return i

def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


t = int(input()) # read a line with a single integer
for i in range(0, t):
    u = int(input())
    input_table=[]
    for j in range(0, u):
        input_line = [int(s) for s in input().split(" ")]
        input_table.append(input_line)
    trace_value = trace(input_table)
    rows_check = matrix_check(input_table)
    transposed = list(map(list, zip(*input_table)))
    columns_check = matrix_check(transposed)

    print("Case #"+str(i+1)+": "+str(trace_value)+" "+str(rows_check)+" "+str(columns_check))
        
