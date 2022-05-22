
nums = [1,2,3,3]
# length  = len(nums)
# n = length/2
hashmap = {}
for ele in nums:
    if ele in hashmap:
        print(ele)
    if ele not in hashmap:
        hashmap[ele] = 1
