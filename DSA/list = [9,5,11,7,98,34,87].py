list = [9,5,11,7,98,34,87]

# sort the list
#sorted_list=[]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if(list[j]>list[i]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

print(list)