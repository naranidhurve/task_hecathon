
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

num=[0,1,0,3,12]
i=0
b=num
while i<len(num):
    b.sort()
    i=i+1
print(b)

