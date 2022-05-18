'''
几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？

给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。

例 1：

输入: m = 3, n = 3, k = 5
输出: 3
解释:
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).
例 2：

输入: m = 2, n = 3, k = 6
输出: 6
解释:
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).
注意：

m 和 n 的范围在 [1, 30000] 之间。
k 的范围在 [1, m * n] 之间。
通过次数11,116提交次数20,339

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

m = 3
n = 3
k = 5

x = 1
y = 1


if n>m:
    print(n,"n")
    for i in range(1,n+1):
        if i*m>=k:
            limit = i
            print(i,m)
            break
else:
    print(m,"m")
    for i in range(1,m+1):
        if i*n>=k:
            limit = i
            print(i,n)
            break
print(limit)
list__ = [x*y   for x in range(limit,n+1) for y in range(1,m+1)]

print(list__)

"""
方法一：二分查找
由于 mm 和 nn 很大，直接求出所有数字然后找到第 kk 小会超出时间限制。不妨考虑一个反向问题：对于乘法表中的数字 xx，它是乘法表中第几小的数字？

求第几小等价于求有多少数字不超过 xx。我们可以遍历乘法表的每一行，对于乘法表的第 ii 行，其数字均为 ii 的倍数，因此不超过 xx 的数字有 \min(\Big\lfloor\dfrac{x}{i}\Big\rfloor,n)min(⌊ 
i
x
​
 ⌋,n) 个，所以整个乘法表不超过 xx 的数字个数为

\sum_{i=1}^{m} \min(\Big\lfloor\dfrac{x}{i}\Big\rfloor,n)
i=1
∑
m
​
 min(⌊ 
i
x
​
 ⌋,n)

由于 i\le \Big\lfloor\dfrac{x}{n}\Big\rfloori≤⌊ 
n
x
​
 ⌋ 时 \Big\lfloor\dfrac{x}{i}\Big\rfloor \ge n⌊ 
i
x
​
 ⌋≥n，上式可化简为

\Big\lfloor\dfrac{x}{n}\Big\rfloor\cdot n + \sum_{i=\Big\lfloor\dfrac{x}{n}\Big\rfloor+1}^{m} \Big\lfloor\dfrac{x}{i}\Big\rfloor
⌊ 
n
x
​
 ⌋⋅n+ 
i=⌊ 
n
x
​
 ⌋+1
∑
m
​
 ⌊ 
i
x
​
 ⌋

由于 xx 越大上式越大，xx 越小上式越小，因此我们可以二分 xx 找到答案，二分的初始边界为乘法表的元素范围，即 [1,mn][1,mn]。

Python3C++JavaC#GolangCJavaScript


作者：LeetCode-Solution
链接：https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/solution/cheng-fa-biao-zhong-di-kxiao-de-shu-by-l-521a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        return bisect_left(range(m * n), k, key=lambda x: x // n * n + sum(x // i for i in range(x // n + 1, m + 1)))

