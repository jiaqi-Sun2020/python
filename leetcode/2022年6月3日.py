"""
给定一个正整数 n，返回 连续正整数满足所有数字之和为 n 的组数 。 

 

示例 1:

输入: n = 5
输出: 2
解释: 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
示例 2:

输入: n = 9
输出: 3
解释: 9 = 4 + 5 = 2 + 3 + 4
示例 3:

输入: n = 15
输出: 4
解释: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
 

提示:

1 <= n <= 109​​​​​​​

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/consecutive-numbers-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


"""

方法一：数学
如果正整数 nn 可以表示成 kk 个连续正整数之和，则由于 kk 个连续正整数之和的最小值是 \sum_{i = 1}^k i = \dfrac{k(k + 1)}{2}∑ 
i=1
k
​
 i= 
2
k(k+1)
​
 ，因此有 n \ge \dfrac{k(k + 1)}{2}n≥ 
2
k(k+1)
​
 ，即 k(k + 1) \le 2nk(k+1)≤2n。枚举每个符合 k(k + 1) \le 2nk(k+1)≤2n 的正整数 kk，判断正整数 nn 是否可以表示成 kk 个连续正整数之和。

如果正整数 nn 可以表示成 kk 个连续正整数之和，假设这 kk 个连续正整数中的最小正整数是 xx，最大正整数是 yy，则有 y = x + k - 1y=x+k−1，根据等差数列求和公式有 n = \dfrac{k(x + y)}{2} = \dfrac{k(2x + k - 1)}{2}n= 
2
k(x+y)
​
 = 
2
k(2x+k−1)
​
 ，x = \dfrac{n}{k} - \dfrac{k - 1}{2}x= 
k
n
​
 − 
2
k−1
​
 ，根据 k(k + 1) \le 2nk(k+1)≤2n 可知 x > 0x>0。分别考虑 kk 是奇数和偶数的情况。

当 kk 是奇数时，k - 1k−1 是偶数，因此 2x + k - 12x+k−1 是正偶数。令 q = \dfrac{2x + k - 1}{2}q= 
2
2x+k−1
​
 ，则 qq 是正整数，n = kqn=kq，q = \dfrac{n}{k}q= 
k
n
​
 。由于 qq 是正整数，因此 nn 可以被 kk 整除。
当 nn 可以被 kk 整除时，由于 \dfrac{n}{k} 
k
n
​
  和 \dfrac{k - 1}{2} 
2
k−1
​
  都是整数，因此 x = \dfrac{n}{k} - \dfrac{k - 1}{2}x= 
k
n
​
 − 
2
k−1
​
  是整数。又由于 x > 0x>0，因此 xx 是正整数。因此 nn 可以表示成 kk 个连续正整数之和。
综上所述，当 kk 是奇数时，「正整数 nn 可以表示成 kk 个连续正整数之和」等价于「正整数 nn 可以被 kk 整除」。

当 kk 是偶数时，2x + k - 12x+k−1 是奇数。将 n = \dfrac{k(2x + k - 1)}{2}n= 
2
k(2x+k−1)
​
  写成 \dfrac{2x + k - 1}{2} = \dfrac{n}{k} 
2
2x+k−1
​
 = 
k
n
​
 ，由于 2x + k - 12x+k−1 是奇数，因此 \dfrac{2x + k - 1}{2} 
2
2x+k−1
​
  不是整数，nn 不可以被 kk 整除，又由于 2x + k - 1 = \dfrac{2n}{k}2x+k−1= 
k
2n
​
  是整数，因此 2n2n 可以被 kk 整除。
当 nn 不可以被 kk 整除且 2n2n 可以被 kk 整除时，\dfrac{2n}{k} 
k
2n
​
  一定是奇数（否则 \dfrac{n}{k} 
k
n
​
  是整数，和 nn 不可以被 kk 整除矛盾），令 \dfrac{2n}{k} = 2t + 1 
k
2n
​
 =2t+1，其中 tt 是整数，则 \dfrac{n}{k} = t + \dfrac{1}{2} 
k
n
​
 =t+ 
2
1
​
 。此时 x = \dfrac{n}{k} - \dfrac{k - 1}{2} = t + \dfrac{1}{2} - \dfrac{k}{2} + \dfrac{1}{2} = t - \dfrac{k}{2} + 1x= 
k
n
​
 − 
2
k−1
​
 =t+ 
2
1
​
 − 
2
k
​
 + 
2
1
​
 =t− 
2
k
​
 +1，由于 \dfrac{k}{2} 
2
k
​
  是整数，因此 xx 是整数。又由于 x > 0x>0，因此 xx 是正整数。因此 nn 可以表示成 kk 个连续正整数之和。
综上所述，当 kk 是偶数时，「正整数 nn 可以表示成 kk 个连续正整数之和」等价于「正整数 nn 不可以被 kk 整除且正整数 2n2n 可以被 kk 整除」。

根据上述分析，可以得到判断正整数 nn 是否可以表示成 kk 个连续正整数之和的方法：

如果 kk 是奇数，则当 nn 可以被 kk 整除时，正整数 nn 可以表示成 kk 个连续正整数之和；

如果 kk 是偶数，则当 nn 不可以被 kk 整除且 2n2n 可以被 kk 整除时，正整数 nn 可以表示成 kk 个连续正整数之和。

Python3JavaC#C++CGolangJavaScript

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        def isKConsecutive(n: int, k: int) -> bool:
            if k % 2:
                return n % k == 0
            return n % k and 2 * n % k == 0

        ans = 0
        k = 1
        while k * (k + 1) <= n * 2:
            if isKConsecutive(n, k):
                ans += 1
            k += 1
        return ans
复杂度分析

时间复杂度：O(\sqrt{n})O( 
n
​
 )，其中 nn 是给定的正整数。当 nn 可以表示成 kk 个连续正整数之和时，kk 不会超过 \sqrt{2n} 
2n
​
 ，因此需要枚举的 kk 的个数是 O(\sqrt{n})O( 
n
​
 )，对于每个枚举的 kk 判断 nn 是否可以表示成 kk 个连续正整数之和的时间是 O(1)O(1)。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/consecutive-numbers-sum/solution/lian-xu-zheng-shu-qiu-he-by-leetcode-sol-33hc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""