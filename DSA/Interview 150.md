

==remove elements from an array which match the target value

k is the length of array without the target elements.

```python
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = len([x for x in nums if x!= val])
        nums[:] = [x for x in nums if x != val]

        return k
```

==remove duplicates from an given array(sorted in ascending order)

```python
    def removeDuplicates(self, nums: List[int]) -> int:
        index  = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index +=1
        return index

```



==Prepare for Design Patterns and Data Structures

1) At least basic definitions 
2) Learn about design Patterns


```python
count = 1
def get_count():
    global count
    for i in (1,2,3):
        count += 1
        
get_count()
print(count)

#Answer is 4
```









