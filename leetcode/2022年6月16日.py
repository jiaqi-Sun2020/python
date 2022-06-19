# nums = [1,2,4,4,3,3,0,9,2,3]
# k = 3
# ret = []
# hashmap = {}
# for i,ele_f in enumerate(nums):
#     for t,ele_s in  enumerate(nums[i+1:]):
#         if abs(ele_f-ele_s)==k:
#             print(i,i+t+1)
#
#             # if i and i+t+1 not in hashmap:
#             #     print("++++++")
#             #     hashmap[i] = 1
#             #     hashmap[i+t+1] = 1
#             ret.append(tuple(sorted([ele_f, ele_s])))
#
#
#
# print(len(set(ret)))
# print(ret)



class Solution:
    def findPairs(self, nums, k) -> int:
        visited, res = set(), set()
        for num in nums:
            if num - k in visited:
                res.add(num - k)
            if num + k in visited:
                res.add(num)
            visited.add(num)
        return len(res)

a = Solution()
print(a.findPairs([1,2,4,4,3,3,0,9,2,3],3))