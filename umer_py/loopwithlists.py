#let x = 30 find its index
nums= [10 , 20 , 30 , 40 , 50]
x = 20

index = 0
for val in nums:
    if(val == x):
        print(f"{x} is found at {index}")
        break
    index+=1

print(nums[1])