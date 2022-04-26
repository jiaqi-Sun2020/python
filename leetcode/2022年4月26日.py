"""
在 n x n 的网格 grid 中，我们放置了一些与 x，y，z 三轴对齐的 1 x 1 x 1 立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

现在，我们查看这些立方体在 xy 、yz 和 zx 平面上的投影。

投影 就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回 所有三个投影的总面积 。

 

示例 1：



输入：[[1,2],[3,4]]
输出：17
解释：这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。
示例 2:

输入：grid = [[2]]
输出：5
示例 3：

输入：[[1,0],[0,2]]
输出：8
 

提示：

n == grid.length == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50
通过次数20,773提交次数27,989

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/projection-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""

grid = [[1,2],[3,4]]
xz_ = 0
xy_ = 0
zy_ = 0
hashmap = {}  #保存列的最大值
for row in grid:
    xz_ += max(row)
    xy_ +=len(row)-row.count(0)
    for i,column in enumerate(row):  #对于每一列
        if i not in hashmap:
            hashmap[i]=column
        else:
            if column > hashmap[i]:
                hashmap[i] = column
for col, max_value in hashmap.items():
    zy_ += max_value
print(xz_,xy_,zy_)

# print(zip(*grid))

"""
for i in zip(*grid):   #zip会把多个列表的相同下标的放在一个元组里面
    print(i)
"""



"""
方法一：数学
思路与算法

根据题意，\texttt{x}x 轴对应行，\texttt{y}y 轴对应列，\texttt{z}z 轴对应网格的数值。

因此：

\texttt{xy}xy 平面的投影面积等于网格上非零数值的数目；
\texttt{yz}yz 平面的投影面积等于网格上每一列最大数值之和；
\texttt{zx}zx 平面的投影面积等于网格上每一行最大数值之和。
返回上述三个投影面积之和。

代码

Python3C++JavaC#CGolangJavaScript

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xyArea = sum(v > 0 for row in grid for v in row)
        yzArea = sum(map(max, zip(*grid)))  # 注意这里为 O(n) 空间复杂度，改为下标枚举则可以 O(1)
        zxArea = sum(map(max, grid))
        return xyArea + yzArea + zxArea
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 是网格的行数或列数。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/projection-area-of-3d-shapes/solution/san-wei-xing-ti-tou-ying-mian-ji-by-leet-d66y/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""