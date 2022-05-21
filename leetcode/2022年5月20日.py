"""
给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。

区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。

返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。

 
示例 1：

输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。
示例 2：

输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。
示例 3：

输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1,2,-1]
解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
 

提示：

1 <= intervals.length <= 2 * 104
intervals[i].length == 2
-106 <= starti <= endi <= 106
每个间隔的起点都 不相同

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-right-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

intervals = [[3,4],[2,3],[1,2]]
hashmap = {}

cont = []
ans = [-1]*(len(intervals))
for i,ele in enumerate(intervals):
    if ele[0]<=ele[1]:
        ele.append(i)
        cont.append(ele)

cont  = sorted(cont)
print(cont)
for place,(start,end,n) in enumerate(cont):
    min_flag = 2 * (10**4)
    place_flag = -1
    for start_,end_,i in cont[place:len(cont)]:
        if end<=start_ and min_flag>=start_:
            min_flag = start_
            place_flag=i
            ans[n]=place_flag

print(ans)
#print(sorted(cont,key=lambda x: x[1]))





"""
方法一：二分查找
思路与算法

最简单的解决方案是对于集合中的每个区间，我们扫描所有区间找到其起点大于当前区间的终点的区间（具有最先差值），时间复杂度为 O(n^2)O(n 
2
 )，在此我们不详细描述。

首先我们可以对区间 \textit{intervals}intervals 的起始位置进行排序，并将每个起始位置 \textit{intervals}[i][0]intervals[i][0] 对应的索引 ii 存储在数组 \textit{startIntervals}startIntervals 中，然后枚举每个区间 ii 的右端点 \textit{intervals}[i][1]intervals[i][1]，利用二分查找来找到大于等于 \textit{intervals}[i][1]intervals[i][1] 的最小值 \textit{val}val 即可，此时区间 ii 对应的右侧区间即为右端点 \textit{val}val 对应的索引。

代码

Python3JavaC++C#CGolangJavaScript

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, interval in enumerate(intervals):
            interval.append(i)
        intervals.sort()

        n = len(intervals)
        ans = [-1] * n
        for _, end, id in intervals:
            i = bisect_left(intervals, [end])
            if i < n:
                ans[id] = intervals[i][2]
        return ans
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 为区间数组的长度。排序的时间为 O(n \log n)O(nlogn)，每次进行二分查找花费的时间为 O(\log n)O(logn)，一共需要进行 nn 次二分查找，因此总的时间复杂度为 O(n \log n)O(nlogn)。

空间复杂度：O(n)O(n)，其中 nn 为区间数组的长度。\textit{startIntervals}startIntervals 一共存储了 nn 个元素，因此空间复杂度为 O(n)O(n)。

方法二：双指针
思路与算法

我们可以开辟两个新的数组：

\textit{startIntervals}startIntervals，基于所有区间的起始点从小到大排序。
\textit{endIntervals}endIntervals，基于所有区间的结束点从小到大排序。
我们从 \textit{endIntervals}endIntervals 数组中取出第 ii 个区间，就可以从左到右扫描 \textit{startIntervals}startIntervals 数组中的区间起点来找到满足右区间条件的区间。设 \textit{endIntervals}endIntervals 数组中第 ii 个元素的右区间为 \textit{startIntervals}startIntervals 数组中的第 jj 个元素，此时可以知道 \textit{startIntervals}[j-1][0] < \textit{endIntervals}[i][1], \textit{startIntervals}[j][0] \ge \textit{endIntervals}[i][1]startIntervals[j−1][0]<endIntervals[i][1],startIntervals[j][0]≥endIntervals[i][1]。当我们遍历 \textit{endIntervals}endIntervals 数组中第 i+1i+1 个元素时，我们不需要从第一个索引开始扫描 \textit{startIntervals}startIntervals 数组，可以直接从第 jj 个元素开始扫描 {startIntervals}startIntervals 数组。由于数组中所有的元素都是已排序，因此可以知道 \textit{startIntervals}[j-1][0] < \textit{endIntervals}[i][1] \le \textit{endIntervals}[i+1][1]startIntervals[j−1][0]<endIntervals[i][1]≤endIntervals[i+1][1]，所以数组 \textit{startIntervals}startIntervals 的前 j-1j−1 的元素的起始点都小于 \textit{endIntervals}[i+1][1]endIntervals[i+1][1]，因此可以直接跳过前 j-1j−1 个元素，只需要从 jj 开始搜索即可。

代码

Python3JavaC++C#CGolangJavaScript

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts, ends = list(zip(*intervals))
        starts = sorted(zip(starts, range(n)))
        ends = sorted(zip(ends, range(n)))

        ans, j = [-1] * n, 0
        for end, id in ends:
            while j < n and starts[j][0] < end:
                j += 1
            if j < n:
                ans[id] = starts[j][1]
        return ans
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 为区间数组的长度。两个数组的排序时间一共为 O(n \log n)O(nlogn)，查找每个区间的右侧区间的时间复杂度为 O(n)O(n)，因此总的时间复杂度为 O(n \log n)O(nlogn)。

空间复杂度：O(n)O(n)，其中 nn 为区间数组的长度。\textit{startIntervals}, \textit{endIntervals}startIntervals,endIntervals 均存储了 nn 个元素，因此空间复杂度为 O(n)O(n)。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/find-right-interval/solution/xun-zhao-you-qu-jian-by-leetcode-solutio-w2ic/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""