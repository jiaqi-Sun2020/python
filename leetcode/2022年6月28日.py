"""
给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

你可以假设所有输入数组都可以得到满足题目要求的结果。

 

示例 1：

输入：nums = [1,5,1,1,6,4]
输出：[1,6,1,5,1,4]
解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。
示例 2：

输入：nums = [1,3,2,2,3,1]
输出：[2,3,1,3,1,2]
 

提示：

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 5000
题目数据保证，对于给定的输入 nums ，总能产生满足题目要求的结果
 

进阶：你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/wiggle-sort-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""
nums = [1,5,1,1,6,4]
nums = [1,3,2,2,3,1]
class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = sorted(nums)
        x = (n + 1) // 2
        j, k = x - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = arr[j]
            if i + 1 < n:
                   nums[i + 1] = arr[k]
            j -= 1
            k -= 1

        return sorted(nums)


a = Solution()
print(a.wiggleSort(nums))

"""
此题为「280. 摆动排序」的扩展题目，不同之处在于本题要求排序后的相邻的元素有严格的大小关系，满足 \textit{nums}[0] < \textit{nums}[1] > \textit{nums}[2] < \textit{nums}[3] \cdotsnums[0]<nums[1]>nums[2]<nums[3]⋯。首先想到的解法即为排序，然后找到满足相邻的严格大小的关系。需要观察一下什么样的数组才能满足题目的要求，可以完成最终的摆动排序。假设数组中元素的数目为 nn，则此时我们可以得到结论数组中相同元素的数目最多不超过 \left\lfloor \dfrac{n + 1}{2} \right\rfloor⌊ 
2
n+1
​
 ⌋，我们可以用反证法来证明。当相同的元素的数目大于 \left\lfloor \dfrac{n + 1}{2} \right\rfloor⌊ 
2
n+1
​
 ⌋，此时无论如何摆放都会有相同的元素相邻，必然导致摆动排序无法完成。将数组按照从小到大进行排序后，令 x = \left\lfloor \dfrac{n + 1}{2} \right\rfloorx=⌊ 
2
n+1
​
 ⌋，此时根据前面的推论可以推测 \textit{nums}[i] \neq \textit{nums}[i+x]nums[i] 

​
 =nums[i+x]，则一定满足 \textit{nums}[i] < \textit{nums}[i+x]nums[i]<nums[i+x]，因此我们可以得到：

\textit{nums}[0] < \textit{nums}[x],\textit{nums}[1] < \textit{nums}[x+1], \cdots,\textit{nums}[i] < \textit{nums}[i+x]
nums[0]<nums[x],nums[1]<nums[x+1],⋯,nums[i]<nums[i+x]

此时我们可以利用上述关系完成数组的摆动排列。我们分两种情况来讨论：

当 nn 为偶数时：因为 \textit{nums}[i] < \textit{nums}[i+x]nums[i]<nums[i+x]，所以一定满足 \textit{nums}[i] < \textit{nums}[i+x], \textit{nums}[i-1] < \textit{nums}[i+x]nums[i]<nums[i+x],nums[i−1]<nums[i+x]，因此我们将 \textit{nums}[i+x]nums[i+x] 插入到 \textit{nums}[i]nums[i] 与 \textit{nums}[i-1]nums[i−1] 之间，比如我们可以按照以下顺序进行插入：

\textit{nums}[x], \textit{nums}[0], \textit{nums}[x + 1], \textit{nums}[1],\cdots, \textit{nums}[n-2-x],\textit{nums}[n-1],\textit{nums}[n-1-x]
nums[x],nums[0],nums[x+1],nums[1],⋯,nums[n−2−x],nums[n−1],nums[n−1−x]

然后将上述序列进行反转：

\textit{nums}[n-1-x], \textit{nums}[n-1], \textit{nums}[n-2-x], \cdots, \textit{nums}[1], \textit{nums}[x + 1], \textit{nums}[0], \textit{nums}[x]
nums[n−1−x],nums[n−1],nums[n−2−x],⋯,nums[1],nums[x+1],nums[0],nums[x]

即可得到合法的摆动排序。比如序列当前序列为 [0,1,2,3,4,5][0,1,2,3,4,5]，我们可以得到序列 [3,0,4,1,5,2][3,0,4,1,5,2]，然后将其反转即为 [2,5,1,4,0,3][2,5,1,4,0,3]。

当 nn 为奇数时：此时情况稍微复杂一些，此时我们需要证明当满足 i > 0i>0 时，nums[i] < nums[i+x-1]nums[i]<nums[i+x−1]。此时我们可以用反证法来证明。假设存在 ii 且满足 i > 0i>0，且满足 \textit{nums}[i] = \textit{nums}[i+x-1]nums[i]=nums[i+x−1] 时，则此时按照排序的规则可知 \textit{nums}[i] = \textit{nums}[i+1] = \textit{nums}[i+2] = \cdots = \textit{nums}[i+x-1]nums[i]=nums[i+1]=nums[i+2]=⋯=nums[i+x−1]，此时数组中一共有 xx 个相同的元素。由于这 xx 个元素不能互相相邻，按照摆动排序的规则，这 xx 个相同的元素只能放在数组的偶数位的索引中（数组索引以 00 为起始），只能放置在 0,2,4,\cdots,n-10,2,4,⋯,n−1 位置上，否则就会出现相邻元素相等，而此时由于 \textit{nums}[0]nums[0] 最小，因此它只能放置在偶数位的索引上，而数组中的偶数位的索引最多只有 xx 个，这就必然会导致矛盾，\textit{nums}[0]nums[0] 无法摆放。因此，当满足 i > 0i>0 时，nums[i] \neq nums[i+x-1]nums[i] 

​
 =nums[i+x−1]，也即 \textit{nums}[i] < \textit{nums}[i+x-1]nums[i]<nums[i+x−1]。根据上述的结论我们可以得到 \textit{nums}[i] < \textit{nums}[i+x]，\textit{nums}[i+1] < \textit{nums}[i+x]nums[i]<nums[i+x]，nums[i+1]<nums[i+x]。因此我们将 \textit{nums}[i+x]nums[i+x] 插入到 \textit{nums}[i]nums[i] 与 \textit{nums}[i+1]nums[i+1] 之间，比如我们可以按照以下顺序进行插入：

\textit{nums}[0], \textit{nums}[x], \textit{nums}[1],\cdots, \textit{nums}[n-1-x],\textit{nums}[n-1],\textit{nums}[n-x]
nums[0],nums[x],nums[1],⋯,nums[n−1−x],nums[n−1],nums[n−x]

比如序列当前序列为 [0,1,2,3,4][0,1,2,3,4]，我们可以返回序列 [0,3,1,4,2][0,3,1,4,2]。同理我们将上述序列进行反转后，该序列仍然为符合要求的摆动排序。

按照上述规则返回插入的序列即可。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/wiggle-sort-ii/solution/bai-dong-pai-xu-ii-by-leetcode-solution-no0s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""