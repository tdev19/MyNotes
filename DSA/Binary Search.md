

```


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

# binary search

def binary_search(list1,num,low,high):
    
    while low<=high:
        mid = int((low+high)//2)
        #print(mid)
        if(list1[mid]==num):
            return mid
        elif(num > list1[mid]):
            high = mid - 1
        else:
            low = mid + 1

num1 = 5
print(binary_search(list,num1,0,len(list) - 1))
            
        
```

Difference between list and array


lists 
- can have different types of elements
- are resizable
- are indexed
Arrays
- have same type of elements and need to be defined while declaring array
- have fixed size
- are also indexed
- are not a built in python data structure. It needs to be imported.


	