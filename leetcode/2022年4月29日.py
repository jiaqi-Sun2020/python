List = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]

n = len(List)
def forth_split(list__,len__):    #输入是一个矩阵,和一个矩阵的长宽  输出的是
    half = len__//2
    one_value =  half*half
    block_value = 0
    ret = []
    for i in range(4):   #对获取的模块进行分割成四块
        contain = []
        block_sum = 0
        if i ==0:
            x = 0
            y = 0
            rowhalf =  list__[y*half:(y+1)*half]
            for ele in rowhalf:
                contain.append(ele[x*half:(x+1)*half])
            # print(contain)
            block_sum = sum(map(sum,contain))
            if block_sum==one_value:
                ret.append([1,1])
            elif block_sum==0:
                ret.append([1, 0])
            else:
                ret.append([0, 1])
        if i==1:
            x = 1
            y = 0
            rowhalf =  list__[y*half:(y+1)*half]
            for ele in rowhalf:
                contain.append(ele[x*half:(x+1)*half])
            # print(contain)
            block_sum = sum(map(sum, contain))
            if block_sum == one_value:
                ret.append([1, 1])
            elif block_sum == 0:
                ret.append([1, 0])
            else:
                ret.append([0, 1])
        if i==2:
            x = 0
            y = 1
            rowhalf =  list__[y*half:(y+1)*half]
            for ele in rowhalf:
                contain.append(ele[x*half:(x+1)*half])
            # print(contain)
            block_sum = sum(map(sum, contain))
            if block_sum == one_value:
                ret.append([1, 1])
            elif block_sum == 0:
                ret.append([1, 0])
            else:
                ret.append([0, 1])
        if i==3:
            x = 1
            y = 1
            rowhalf =  list__[y*half:(y+1)*half]
            for ele in rowhalf:
                contain.append(ele[x*half:(x+1)*half])
            # print(contain)
            block_sum = sum(map(sum, contain))
            if block_sum == one_value:
                ret.append([1, 1])
            elif block_sum == 0:
                ret.append([1, 0])
            else:
                ret.append([0, 1])
    return ret
print(forth_split(List,n))


"""
方法一：递归
思路与算法

我们可以使用递归的方法构建出四叉树。

具体地，我们用递归函数 \text{dfs}(r_0, c_0, r_1, c_1)dfs(r 
0
​
 ,c 
0
​
 ,r 
1
​
 ,c 
1
​
 ) 处理给定的矩阵 \textit{grid}grid 从 r_0r 
0
​
  行开始到 r_1-1r 
1
​
 −1 行，从 c_0c 
0
​
  和 c_1-1c 
1
​
 −1 列的部分。我们首先判定这一部分是否均为 00 或 11，如果是，那么这一部分对应的是一个叶节点，我们构造出对应的叶节点并结束递归；如果不是，那么这一部分对应的是一个非叶节点，我们需要将其分成四个部分：行的分界线为 \dfrac{r_0+r_1}{2} 
2
r 
0
​
 +r 
1
​
 
​
 ，列的分界线为 \dfrac{c_0+c_1}{2} 
2
c 
0
​
 +c 
1
​
 
​
 ，根据这两条分界线递归地调用 \text{dfs}dfs 函数得到四个部分对应的树，再将它们对应地挂在非叶节点的四个子节点上。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/construct-quad-tree/solution/jian-li-si-cha-shu-by-leetcode-solution-gcru/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r0: int, c0: int, r1: int, c1: int) -> 'Node':
            if all(grid[i][j] == grid[r0][c0] for i in range(r0, r1) for j in range(c0, c1)):
                return Node(grid[r0][c0] == 1, True)
            return Node(
                True,
                False,
                dfs(r0, c0, (r0 + r1) // 2, (c0 + c1) // 2),
                dfs(r0, (c0 + c1) // 2, (r0 + r1) // 2, c1),
                dfs((r0 + r1) // 2, c0, r1, (c0 + c1) // 2),
                dfs((r0 + r1) // 2, (c0 + c1) // 2, r1, c1),
            )
        return dfs(0, 0, len(grid), len(grid))
"""