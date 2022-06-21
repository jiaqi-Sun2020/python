"""
Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 半开区间 的范围并查询它们。

半开区间 [left, right) 表示所有 left <= x < right 的实数 x 。

实现 RangeModule 类:

RangeModule() 初始化数据结构的对象。
void addRange(int left, int right) 添加 半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。
boolean queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true ，否则返回 false 。
void removeRange(int left, int right) 停止跟踪 半开区间 [left, right) 中当前正在跟踪的每个实数。
 

示例 1：

输入
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
输出
[null, null, null, true, false, true]

解释
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); 返回 true （区间 [10, 14) 中的每个数都正在被跟踪）
rangeModule.queryRange(13, 15); 返回 false（未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
rangeModule.queryRange(16, 17); 返回 true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
 

提示：

1 <= left < right <= 109
在单个测试用例中，对 addRange 、  queryRange 和 removeRange 的调用总数不超过 104 次
通过次数5,969提交次数12,271

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/range-module
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


"""
方法一：有序集合 / 有序映射
思路与算法

我们可以使用有序集合或者有序映射来实时维护所有的区间。在任意一次 \text{addRange}addRange 或 \text{removeRange}removeRange 操作后，我们需要保证有序集合中的区间两两不能合并成一个更大的连续区间。也就是说：如果当前有序集合中有 kk 个区间 [l_1, r_1), [l_2, r_2), \cdots, [l_k, r_k)[l 
1
​
 ,r 
1
​
 ),[l 
2
​
 ,r 
2
​
 ),⋯,[l 
k
​
 ,r 
k
​
 )，那么需要保证：

l_1 < r_1 < l_2 < r_2 < \cdots < l_k < r_k
l 
1
​
 <r 
1
​
 <l 
2
​
 <r 
2
​
 <⋯<l 
k
​
 <r 
k
​
 

成立。这样一来 \text{queryRange}queryRange 操作就会变得非常方便：对于 \text{queryRange(left, right)}queryRange(left, right) 而言，我们只需要判断是否存在一个区间 [l_i, r_i)[l 
i
​
 ,r 
i
​
 )，满足 l_i \leq \textit{left} < \textit{right} \leq r_il 
i
​
 ≤left<right≤r 
i
​
  即可。

接下来我们详细讲解如何处理 \text{addRange}addRange 或 \text{removeRange}removeRange 和操作。对于 \text{addRange(left, right)}addRange(left, right) 操作，我们首先在有序集合上进行二分，找出最后一个满足 l_i \leq \textit{left}l 
i
​
 ≤left 的区间 [l_i, r_i)[l 
i
​
 ,r 
i
​
 )，那么会有如下的四种情况：

如果不存在这样的区间，那么我们可以忽略这一步；

如果 l_i \leq \textit{left} < \textit{right} \leq r_il 
i
​
 ≤left<right≤r 
i
​
 ，即 [l_i, r_i)[l 
i
​
 ,r 
i
​
 ) 完全包含待添加的区间，那么我们不需要进行任何操作，可以直接返回；

如果 l_i \leq \textit{left} \leq r_i < \textit{right}l 
i
​
 ≤left≤r 
i
​
 <right，我们需要删除区间 [l_i, r_i)[l 
i
​
 ,r 
i
​
 )，并把 \textit{left}left 置为 l_il 
i
​
 。此时 [\textit{left}, \textit{right})[left,right) 就表示待添加区间与 [l_i, r_i)[l 
i
​
 ,r 
i
​
 ) 的并集；

如果 l_i < r_i < \textit{left} < \textit{right}l 
i
​
 <r 
i
​
 <left<right，那么我们也可以忽略这一步。

随后，我们遍历 [l_i, r_i)[l 
i
​
 ,r 
i
​
 ) 之后的区间（如果前面不存在满足要求的 [l_i, r_i)[l 
i
​
 ,r 
i
​
 )，那么就从头开始遍历），这些区间 [l_j, r_j)[l 
j
​
 ,r 
j
​
 ) 都满足 l_j > \textit{left}l 
j
​
 >left，那么只要 l_j \leq \textit{right}l 
j
​
 ≤right，[l_j, r_j)[l 
j
​
 ,r 
j
​
 ) 就可以与 [\textit{left}, \textit{right})[left,right) 合并成一个更大的连续区间。当遍历到 l_j > \textit{right}l 
j
​
 >right 时，根据集合的有序性，之后的所有区间都不会和 [\textit{left}, \textit{right})[left,right) 有交集，就可以结束遍历。

在遍历完成后，我们还需要将 [\textit{left}, \textit{right})[left,right) 加入有序集合中。

对于 \text{removeRange(left, right)}removeRange(left, right) 操作，我们的处理方法是类似的，首先在有序集合上进行二分，找出最后一个满足 l_i \leq \textit{left}l 
i
​
 ≤left 的区间 [l_i, r_i)[l 
i
​
 ,r 
i
​
 )，那么会有如下的四种情况：

如果不存在这样的区间，那么我们可以忽略这一步；

如果满足 l_i \leq \textit{left} \leq \textit{right} \leq r_il 
i
​
 ≤left≤right≤r 
i
​
 ，即 [l_i, r_i)[l 
i
​
 ,r 
i
​
 ) 完全包含待添加的区间，那么 l_i \leq \textit{left} \leq \textit{right} \leq r_il 
i
​
 ≤left≤right≤r 
i
​
  的删除会导致 [l_i, r_i)[l 
i
​
 ,r 
i
​
 ) 变成两个短区间：[l_i, \textit{left})[l 
i
​
 ,left) 和 [\textit{right}, r_i)[right,r 
i
​
 )。如果 \textit{left} = l_ileft=l 
i
​
 ，那么第一个区间为空区间；如果 \textit{right} = r_iright=r 
i
​
 ，那么第二个区间为空区间。我们将 [l_i, r_i)[l 
i
​
 ,r 
i
​
 ) 删除后，向有序集合中添加所有的非空区间，即可直接返回；

如果 l_i \leq \textit{left} < r_i < \textit{right}l 
i
​
 ≤left<r 
i
​
 <right，我们把区间 [l_i, r_i)[l 
i
​
 ,r 
i
​
 ) 变成 [l_i, \textit{left})[l 
i
​
 ,left) 即可；

如果 l_i < r_i \leq \textit{left} < \textit{right}l 
i
​
 <r 
i
​
 ≤left<right，那么我们也可以忽略这一步。

随后，我们遍历 [l_i, r_i)[l 
i
​
 ,r 
i
​
 ) 之后的区间，这些区间 [l_j, r_j)[l 
j
​
 ,r 
j
​
 ) 都满足 l_j > \textit{left}l 
j
​
 >left，那么只要 l_j < \textit{right}l 
j
​
 <right，[l_j, r_j)[l 
j
​
 ,r 
j
​
 ) 中的一部分就会被删除。如果 r_j \leq \textit{right}r 
j
​
 ≤right，那么 [l_j, r_j)[l 
j
​
 ,r 
j
​
 ) 会被完全删除；如果 r_j > \textit{right}r 
j
​
 >right，那么 [l_j, r_j)[l 
j
​
 ,r 
j
​
 ) 会剩下 [\textit{right}, r_j)[right,r 
j
​
 )，此时之后的所有区间都不会和 [\textit{left}, \textit{right})[left,right) 有交集，就可以结束遍历。

最后，对于 \text{queryRange(left, right)}queryRange(left, right) 操作，我们同样在有序集合上进行二分，找出最后一个满足 l_i \leq \textit{left}l 
i
​
 ≤left 的区间 [l_i, r_i)[l 
i
​
 ,r 
i
​
 )。如果 l_i \leq \textit{left} < \textit{right} \leq r_il 
i
​
 ≤left<right≤r 
i
​
 ，那么返回 \text{True}True，否则返回 \text{False}False。

代码

C++JavaPython3Golang

class RangeModule {
public:
    RangeModule() {}
    
    void addRange(int left, int right) {
        auto it = intervals.upper_bound(left);
        if (it != intervals.begin()) {
            auto start = prev(it);
            if (start->second >= right) {
                return;
            }
            if (start->second >= left) {
                left = start->first;
                intervals.erase(start);
            }
        }
        while (it != intervals.end() && it->first <= right) {
            right = max(right, it->second);
            it = intervals.erase(it);
        }
        intervals[left] = right;
    }
    
    bool queryRange(int left, int right) {
        auto it = intervals.upper_bound(left);
        if (it == intervals.begin()) {
            return false;
        }
        it = prev(it);
        return right <= it->second;
    }
    
    void removeRange(int left, int right) {
        auto it = intervals.upper_bound(left);
        if (it != intervals.begin()) {
            auto start = prev(it);
            if (start->second >= right) {
                int ri = start->second;
                if (start->first == left) {
                    intervals.erase(start);
                }
                else {
                    start->second = left;
                }
                if (right != ri) {
                    intervals[right] = ri;
                }
                return;
            }
            else if (start->second > left) {
                start->second = left;
            }
        }
        while (it != intervals.end() && it->first < right) {
            if (it->second <= right) {
                it = intervals.erase(it);
            }
            else {
                intervals[right] = it->second;
                intervals.erase(it);
                break;
            }
        }
    }

private:
    map<int, int> intervals;
};
复杂度分析

时间复杂度：对于操作 \text{queryRange}queryRange，时间复杂度为 O(\log(a+r))O(log(a+r))，其中 aa 是操作 \text{addRange}addRange 的次数，rr 是操作 \text{removeRange}removeRange 的次数。对于操作 \text{addRange}addRange 和 \text{removeRange}removeRange，时间复杂度为均摊 O(\log(a+r))O(log(a+r))，这是因为 \text{addRange}addRange 操作最多添加一个区间，\text{removeRange}removeRange 最多添加两个区间，每一个添加的区间只会在未来的操作中被移除一次，因此均摊时间复杂度为对有序集合 / 有序映射常数次操作需要的时间，即为 O(\log(a+r))O(log(a+r))。

空间复杂度：O(a+r)O(a+r)，即为有序集合 / 有序映射需要使用的空间。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/range-module/solution/range-mo-kuai-by-leetcode-solution-4utf/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

from sortedcontainers import SortedDict


class RangeModule:

    def __init__(self):
        self.intervals = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x != 0:
            start = x - 1
            if itvs_.values()[start] >= right:
                return
            if itvs_.values()[start] >= left:
                left = itvs_.keys()[start]
                itvs_.popitem(start)
                x -= 1

        while x < len(itvs_) and itvs_.keys()[x] <= right:
            right = max(right, itvs_.values()[x])
            itvs_.popitem(x)

        itvs_[left] = right

    def queryRange(self, left: int, right: int) -> bool:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x == 0:
            return False

        return right <= itvs_.values()[x - 1]

    def removeRange(self, left: int, right: int) -> None:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x != 0:
            start = x - 1
            if (ri := itvs_.values()[start]) >= right:
                if (li := itvs_.keys()[start]) == left:
                    itvs_.popitem(start)
                else:
                    itvs_[li] = left
                if right != ri:
                    itvs_[right] = ri
                return
            elif ri > left:
                itvs_[itvs_.keys()[start]] = left

        while x < len(itvs_) and itvs_.keys()[x] < right:
            if itvs_.values()[x] <= right:
                itvs_.popitem(x)
            else:
                itvs_[right] = itvs_.values()[x]
                itvs_.popitem(x)
                break





