

"""
给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

 

示例 1：



输入: root = [5,2,-3]
输出: [2,-3,4]
示例 2：



输入: root = [5,2,-5]
输出: [2]
 

提示:

节点数在 [1, 104] 范围内
-105 <= Node.val <= 105

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/most-frequent-subtree-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""



"""
方法一：深度优先搜索
我们可以从根结点出发，深度优先搜索这棵二叉树。对于每棵子树，其子树元素和等于子树根结点的元素值，加上左子树的元素和，以及右子树的元素和。

用哈希表统计每棵子树的元素和的出现次数，计算出现次数的最大值 \textit{maxCnt}maxCnt，最后将出现次数等于 \textit{maxCnt}maxCnt 的所有元素和返回。

Python3C++JavaC#GolangJavaScriptC


作者：LeetCode-Solution
链接：https://leetcode.cn/problems/most-frequent-subtree-sum/solution/chu-xian-ci-shu-zui-duo-de-zi-shu-yuan-s-kdjc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnt = Counter()
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            sum = node.val + dfs(node.left) + dfs(node.right)
            cnt[sum] += 1
            return sum
        dfs(root)

        maxCnt = max(cnt.values())
        return [s for s, c in cnt.items() if c == maxCnt]
