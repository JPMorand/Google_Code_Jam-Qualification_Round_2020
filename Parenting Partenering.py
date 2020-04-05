t=int(input())
for i in range(0, t):
    u = int(input())
    input_table=[]
    for j in range(0, u):
        input_line = [int(s) for s in input().split(" ")]
        input_line.append(j)
        input_table.append(input_line)

    max_j=0
    max_c=0

    t_j=[]
    t_c=[]
    allocation = ""
    sorted_table=sorted(input_table, key=lambda x: x[0])
    flag = 0
    for time in sorted_table:
        if max_j>max_c:
            if time[0]>=max_c:
                t_c.append(time[2])
                max_c=time[1]
            else:
                print("Case #"+str(i+1)+": IMPOSSIBLE") #see how to skip k for loop
                flag = 1
                break
                
        else:
            if time[0]>=max_j:
                t_j.append(time[2])
                max_j=time[1]
            else:
                print("Case #"+str(i+1)+": IMPOSSIBLE") #see how to skip k for loop
                flag = 1
                break    
    if flag==0:
        for z in range(0, u):
            if z in t_j:
                allocation += "J"
            else:
                allocation += "C"
                
        print("Case #"+str(i+1)+": "+allocation)

