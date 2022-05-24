"""
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。

 

示例 1：



输入：[1,1,1,1,1,null,1]
输出：true
示例 2：



输入：[2,2,2,5,2]
输出：false
 

提示：

给定树的节点数范围是 [1, 100]。
每个节点的值都是整数，范围为 [0, 99] 。
通过次数48,961提交次数69,383

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/univalued-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

方法一：深度优先搜索
思路与算法

一棵树的所有节点都有相同的值，当且仅当对于树上的每一条边的两个端点，它们都有相同的值（这样根据传递性，所有节点都有相同的值）。

因此，我们可以对树进行一次深度优先搜索。当搜索到节点 xx 时，我们检查 xx 与 xx 的每一个子节点之间的边是否满足要求。例如对于左子节点而言，如果其存在并且值与 xx 相同，那么我们继续向下搜索该左子节点；如果值与 xx 不同，那么我们直接返回 \text{False}False。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/univalued-binary-tree/solution/dan-zhi-er-cha-shu-by-leetcode-solution-15bn/
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
    def isUnivalTree(self, root: TreeNode) -> bool:
        ret= True
        if not root:
            return True
        if root.left:
            if root.left.val != root.val or not self.isUnivalTree(root.left):
                return False
        if root.right:
            if root.right.val != root.val or not self.isUnivalTree(root.right):
                return False
        return True






