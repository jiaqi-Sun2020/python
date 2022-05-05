"""
给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
 

示例 1：

输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
示例 2：

输入：nums = [1,2,3], k = 0
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-product-less-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
k = 19
# nums = [1,2,3]
# k = 0
# nums = [10,5,2,6]
# k = 100
ret = []
for i in range(len(nums)):
    block = []
    place = i
    if nums[place]<k:
        m = nums[place]
        ret.append([m])
        block.append(m)
    else:
        continue
    while m<k and place<len(nums)-1:

        m = m * nums[place+1]
        if m >= k:
            continue

        place += 1
        # ret.append(block[:])
        block.append(nums[place])
        ret.append(block[:])
print(ret)
print(len(ret))


"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, prod, i = 0, 1, 0
        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            ans += j - i + 1
        return ans
"""
