def split(word): 
    return list(word)
#Read file
t = int(input()) # read a line with a single integer
input_table=[]
for i in range(0, t):
    input_line = split(input())
    input_table.append(input_line)

for j in range(len(input_table)):
    for k in range(len(input_table[j])):
        digit = input_table[j][k]
        input_table[j][k] = "("*int(digit)+digit+int(digit)*")"
    input_table[j] = ''.join(str(l) for l in input_table[j])
    while ")(" in input_table[j]:
        input_table[j] = "".join(input_table[j].splitlines()).replace(')(', '')
    print("Case #"+str(j+1)+": "+input_table[j])
