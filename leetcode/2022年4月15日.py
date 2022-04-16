"""
给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果 NestedInteger 。

列表中的每个元素只可能是整数或整数嵌套列表

 

示例 1：

输入：s = "324",
输出：324
解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
示例 2：

输入：s = "[123,[456,[789]]]",
输出：[123,[456,[789]]]
解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
1. 一个 integer 包含值 123
2. 一个包含两个元素的嵌套列表：
    i.  一个 integer 包含值 456
    ii. 一个包含一个元素的嵌套列表
         a. 一个 integer 包含值 789
 

提示：

1 <= s.length <= 5 * 104
s 由数字、方括号 "[]"、负号 '-' 、逗号 ','组成
用例保证 s 是可解析的 NestedInteger
输入中的所有值的范围是 [-106, 106]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/mini-parser
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


# class Solution:
#     def deserialize(self, s: str) -> NestedInteger:


# print(eval("324"))
import numpy as np
# print(eval("[123,[456,[789]]]"))


def deserialize(s):
            ret = []
            size  =  s.count("]")
            if size == 0:
                return (int(s))
            list_ = s.split(",")
            for i,li in enumerate(list_):
                list_[size-i-1] = list_[size-i-1].replace("[","")
                list_[size-i-1] = list_[size-i-1].replace("]","")
                #ret[-1].append(NestedInteger(int(eval(list_[size-i-1]))))
                ret[-1].add(int(eval(list_[size - i - 1])))





# print(deserialize(s = "[123,[456,[789]]]"))



c = {"a"}
c.add(3)
print(type(c))


























"""
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # 纯数字
        if s[0] != '[':
            return NestedInteger(int(s))
        stack, curVal, sign = [], 0, False
        for i, c in enumerate(s):
            match c:
                case '[':
                    # 递归嵌套
                    stack.append(NestedInteger())
                case '-':
                    # 数字符号
                    sign = True
                case ',':
                    # 只有上一个字符是数字才加入了新的数字，否则可能是 "],"
                    if s[i - 1].isdigit():
                        stack[-1].add(NestedInteger(-curVal if sign else curVal))
                    curVal, sign = 0, False
                case ']':
                    # 只有上一个字符是数字才加入了新的数字，否则可能是 "[]"
                    if s[i - 1].isdigit():
                        stack[-1].add(NestedInteger(-curVal if sign else curVal))
                    # 弹出栈，并将当前的对象加入嵌套的列表中
                    if len(stack) > 1:
                        cur = stack.pop()
                        stack[-1].add(cur)
                    curVal, sign = 0, False
                case _:
                    # 数字计算
                    curVal = curVal * 10 + int(c)
        return stack.pop()

作者：himymBen
链接：https://leetcode-cn.com/problems/mini-parser/solution/pythonjavajavascriptgo-by-himymben-os66/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""