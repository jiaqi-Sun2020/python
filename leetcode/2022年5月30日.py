"""
给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。

例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

返回这些数字之和。题目数据保证答案是一个 32 位 整数。

 

示例 1：


输入：root = [1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
示例 2：

输入：root = [0]
输出：0
 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], val: int) -> int:
            if node is None:
                return 0
            val = (val << 1) | node.val
            if node.left is None and node.right is None:
                return val
            return dfs(node.left, val) + dfs(node.right, val)
        return dfs(root, 0)
