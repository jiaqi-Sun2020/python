"""
给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

示例:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
solution.pick(3);

// pick(1) 应该返回 0。因为只有nums[0]等于1。
solution.pick(1);

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/random-pick-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


nums = [1,2,3,3,3]
target = 3
import random
class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.all_arg = []

    def pick(self, target: int) -> int:
        for i, ele in enumerate(self.nums):
            if ele ==target:
                self.all_arg.append(i)
        select  = random.randint(0,len(self.all_arg)-1)
        print(self.all_arg[select])

# obj = Solution(nums)
# param_1 = obj.pick(target)

print(random.choice(nums))


"""
方法一：哈希表
如果不考虑数组的大小，我们可以在构造函数中，用一个哈希表 \textit{pos}pos 记录 \textit{nums}nums 中相同元素的下标。

对于 \text{pick}pick 操作，我们可以从 \textit{pos}pos 中取出 \textit{target}target 对应的下标列表，然后随机选择其中一个下标并返回。

Python3C++JavaC#GolangCJavaScript

class Solution:
    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for i, num in enumerate(nums):
            self.pos[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.pos[target])
复杂度分析

时间复杂度：初始化为 O(n)O(n)，\text{pick}pick 为 O(1)O(1)，其中 nn 是 \textit{nums}nums 的长度。

空间复杂度：O(n)O(n)。我们需要 O(n)O(n) 的空间存储 nn 个下标。

方法二：水塘抽样
如果数组以文件形式存储（读者可假设构造函数传入的是个文件路径），且文件大小远超内存大小，我们是无法通过读文件的方式，将所有下标保存在内存中的，因此需要找到一种空间复杂度更低的算法。

我们可以设计如下算法实现 \text{pick}pick 操作：

遍历 \textit{nums}nums，当我们第 ii 次遇到值为 \textit{target}target 的元素时，随机选择区间 [0,i)[0,i) 内的一个整数，如果其等于 00，则将返回值置为该元素的下标，否则返回值不变。

设 \textit{nums}nums 中有 kk 个值为 \textit{target}target 的元素，该算法会保证这 kk 个元素的下标成为最终返回值的概率均为 \dfrac{1}{k} 
k
1
​
 ，证明如下：

\begin{aligned} &P(第\ i\ 次遇到值为\ \textit{target}\ \ 的元素的下标成为最终返回值)\\ =&P(第\ i\ 次随机选择的值= 0) \times P(第\ i+1\ 次随机选择的值\ne 0) \times \cdots \times P(第\ k\ 次随机选择的值\ne 0)\\ =&\dfrac{1}{i} \times (1-\dfrac{1}{i+1}) \times \cdots \times (1-\dfrac{1}{k})\\ =&\dfrac{1}{i} \times \dfrac{i}{i+1} \times \cdots \times \dfrac{k-1}{k}\\ =&\dfrac{1}{k} \end{aligned}
=
=
=
=
​
  
P(第 i 次遇到值为 target  的元素的下标成为最终返回值)
P(第 i 次随机选择的值=0)×P(第 i+1 次随机选择的值 

​
 =0)×⋯×P(第 k 次随机选择的值 

​
 =0)
i
1
​
 ×(1− 
i+1
1
​
 )×⋯×(1− 
k
1
​
 )
i
1
​
 × 
i+1
i
​
 ×⋯× 
k
k−1
​
 
k
1
​
 
​
 

Python3C++JavaC#GolangCJavaScript

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1  # 第 cnt 次遇到 target
                if randrange(cnt) == 0:
                    ans = i
        return ans
时间复杂度：初始化为 O(1)O(1)，\text{pick}pick 为 O(n)O(n)，其中 nn 是 \textit{nums}nums 的长度。

空间复杂度：O(1)O(1)。我们只需要常数的空间保存若干变量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/random-pick-index/solution/sui-ji-shu-suo-yin-by-leetcode-solution-ofsq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""