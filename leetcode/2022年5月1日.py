
"""
给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

 

示例 1：



输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]
示例 2：



输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]
 

提示：

每棵树的节点数在 [0, 5000] 范围内
-105 <= Node.val <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root1 = TreeNode(val=2, left=TreeNode(val=1, left=None, right=None), right=TreeNode(val=4, left=None, right=None))
root2 = TreeNode(val=1, left= TreeNode(val= 0, left= None, right= None), right= TreeNode(val= 3, left= None, right= None))
# print(isinstance(root1,TreeNode))

one_tree_list = []
def one_tree(tree):
    if tree == None:
        return 0
    left_tree = isinstance(tree.left, TreeNode)
    right_tree = isinstance(tree.right, TreeNode)
    if not left_tree and not right_tree:
        one_tree_list.append(tree.val)
    elif not left_tree and right_tree:
        one_tree_list.append(tree.val)
        one_tree(tree.right)
    elif not right_tree and left_tree:
        one_tree_list.append(tree.val)
        one_tree(tree.left)
    elif right_tree and left_tree:
        one_tree_list.append(tree.val)
        one_tree(tree.left)
        one_tree(tree.right)

one_tree(root1)
one_tree(root2)
print(sorted(one_tree_list))



"""
方法一：中序遍历 + 归并
回顾二叉搜索树的定义：

当前节点的左子树中的数均小于当前节点的数；
当前节点的右子树中的数均大于当前节点的数；
所有左子树和右子树自身也是二叉搜索树。
根据上述定义，我们可以用中序遍历访问二叉搜索树，即按照访问左子树——根节点——右子树的方式遍历这棵树，而在访问左子树或者右子树的时候也按照同样的方式遍历，直到遍历完整棵树。遍历结束后，就得到了一个有序数组。

由于整个遍历过程天然具有递归的性质，我们可以直接用递归函数来模拟这一过程。具体描述见 94. 二叉树的中序遍历 的 官方题解。

中序遍历这两棵二叉搜索树，可以得到两个有序数组。然后可以使用双指针方法来合并这两个有序数组，这一方法将两个数组看作两个队列，每次从队列头部取出比较小的数字放到结果中（头部相同时可任取一个）。如下面的动画所示：



Python3C++JavaC#GolangCJavaScript

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node: TreeNode, res: List[int]):
            if node:
                inorder(node.left, res)
                res.append(node.val)
                inorder(node.right, res)

        nums1, nums2 = [], []
        inorder(root1, nums1)
        inorder(root2, nums2)

        merged = []
        p1, n1 = 0, len(nums1)
        p2, n2 = 0, len(nums2)
        while True:
            if p1 == n1:
                merged.extend(nums2[p2:])
                break
            if p2 == n2:
                merged.extend(nums1[p1:])
                break
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        return merged
复杂度分析

时间复杂度：O(n+m)O(n+m)，其中 nn 和 mm 分别为两棵二叉搜索树的节点个数。

空间复杂度：O(n+m)O(n+m)。存储数组以及递归时的栈空间均为 O(n+m)O(n+m)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/solution/liang-ke-er-cha-sou-suo-shu-zhong-de-suo-you-yua-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""