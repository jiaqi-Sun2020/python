"""
给定一个长度为 n 的整数数组 nums 。

假设 arrk 是数组 nums 顺时针旋转 k 个位置后的数组，我们定义 nums 的 旋转函数  F 为：

F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
返回 F(0), F(1), ..., F(n-1)中的最大值 。

生成的测试用例让答案符合 32 位 整数。

 

示例 1:

输入: nums = [4,3,2,6]
输出: 26
解释:
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
示例 2:

输入: nums = [100]
输出: 0
 

提示:

n == nums.length
1 <= n <= 105
-100 <= nums[i] <= 100
通过次数16,466提交次数34,058
请问您在哪类招聘中遇到此题？

社招

校招

实习

未遇到


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-function
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

nums = [4,3,2,6]

def f(spin,list__):  #获取到数组
    spin_list = list__[-spin:]+list__[:-spin]   #顺时针变换完成
    sum = 0
    for i in range(len(list__)):
        sum += i*spin_list[i]
    return sum

for t in range(len(nums)):
    num__ = f(t, nums)
    if t==0:
        max_num=num__
    if num__>max_num:
        max_num=num__

print(max_num)



"""
方法一：迭代   数学归纳法!!!

思路

记数组 \textit{nums}nums 的元素之和为 \textit{numSum}numSum。根据公式，可以得到：

F(0) = 0 \times \textit{nums}[0] + 1 \times \textit{nums}[1] + \ldots + (n-1) \times \textit{nums}[n-1]F(0)=0×nums[0]+1×nums[1]+…+(n−1)×nums[n−1]
F(1) = 1 \times \textit{nums}[0] + 2 \times \textit{nums}[1] + \ldots + 0 \times \textit{nums}[n-1] = F(0) + \textit{numSum} - n \times \textit{nums}[n-1]F(1)=1×nums[0]+2×nums[1]+…+0×nums[n−1]=F(0)+numSum−n×nums[n−1]
更一般地，当 1 \le k \lt n1≤k<n 时，F(k) = F(k-1) + \textit{numSum} - n \times \textit{nums}[n-k]F(k)=F(k−1)+numSum−n×nums[n−k]。我们可以不停迭代计算出不同的 F(k)F(k)，并求出最大值。

代码

Python3JavaC#C++CJavaScriptGolang

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f, n, numSum = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            f += i * num
        res = f
        for i in range(n - 1, 0, -1):
            f = f + numSum - n * nums[i]
            res = max(res, f)
        return res
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。计算 \textit{numSum}numSum 和第一个 ff 消耗 O(n)O(n) 时间，后续迭代 n-1n−1 次 ff 消耗 O(n)O(n) 时间。

空间复杂度：O(1)O(1)。仅使用常数空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/rotate-function/solution/xuan-zhuan-shu-zu-by-leetcode-solution-s0wd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





"""