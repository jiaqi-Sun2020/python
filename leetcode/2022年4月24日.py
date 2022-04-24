"""
给定一个正整数 n，找到并返回 n 的二进制表示中两个 相邻 1 之间的 最长距离 。如果不存在两个相邻的 1，返回 0 。

如果只有 0 将两个 1 分隔开（可能不存在 0 ），则认为这两个 1 彼此 相邻 。两个 1 之间的距离是它们的二进制表示中位置的绝对差。例如，"1001" 中的两个 1 的距离为 3 。

 

示例 1：

输入：n = 22
输出：2
解释：22 的二进制是 "10110" 。
在 22 的二进制表示中，有三个 1，组成两对相邻的 1 。
第一对相邻的 1 中，两个 1 之间的距离为 2 。
第二对相邻的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。
示例 2：

输入：n = 8
输出：0
解释：8 的二进制是 "1000" 。
在 8 的二进制表示中没有相邻的两个 1，所以返回 0 。
示例 3：

输入：n = 5
输出：2
解释：5 的二进制是 "101" 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-gap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


n = 8
string__ = str(bin(n))[2:]
print(string__)
last_place = None
between = 0
for i ,string_ in enumerate(string__):
    if string_=="1":
        if last_place==None:
            last_place = i

        else:
            if between < i - last_place:
                between = i - last_place
            last_place = i

print(between)



"""
方法一：位运算
思路与算法

我们可以使用一个循环从 nn 二进制表示的低位开始进行遍历，并找出所有的 11。我们用一个变量 \textit{last}last 记录上一个找到的 11 的位置。如果当前在第 ii 位找到了 11，那么就用 i - \textit{last}i−last 更新答案，再将 \textit{last}last 更新为 ii 即可。

在循环的每一步中，我们可以使用位运算 \texttt{n \& 1}n & 1 获取 nn 的最低位，判断其是否为 11。在这之后，我们将 nn 右移一位：\texttt{n = n >> 1}n = n >> 1，这样在第 ii 步时，\texttt{n \& 1}n & 1 得到的就是初始 nn 的第 ii 个二进制位。

代码

Python3C++JavaC#CGolangJavaScript

class Solution:
    def binaryGap(self, n: int) -> int:
        last, ans, i = -1, 0, 0
        while n:
            if n & 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
            n >>= 1
            i += 1
        return ans
复杂度分析

时间复杂度：O(\log n)O(logn)。循环中的每一步 nn 会减少一半，因此需要 O(\log n)O(logn) 次循环。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/binary-gap/solution/er-jin-zhi-jian-ju-by-leetcode-solution-dh2q/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

