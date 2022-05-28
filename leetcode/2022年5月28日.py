"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, stack = "", []
        for c in s:
            if c == ')':
                stack.pop()
            if stack:
                res += c
            if c == '(':
                stack.append(c)
        return res

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/remove-outermost-parentheses/solution/shan-chu-zui-wai-ceng-de-gua-hao-by-leet-sux0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, level = "", 0
        for c in s:
            if c == ')':
                level -= 1
            if level:
                res += c
            if c == '(':
                level += 1
        return res

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/remove-outermost-parentheses/solution/shan-chu-zui-wai-ceng-de-gua-hao-by-leet-sux0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



有效括号字符串为空 ""、"(" + A + ")" 或 A + B ，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。

例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
如果有效字符串 s 非空，且不存在将其拆分为 s = A + B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。

给出一个非空有效字符串 s，考虑将其进行原语化分解，使得：s = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。

对 s 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 s 。

 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-outermost-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。






"""

#出栈入栈的简单题目!!!!!

s = "()()"
place = [0]
stack = []
for i, ele in enumerate(s):
    if ele == "(":
        stack.append(1)
    else:
        stack.pop()
    if len(stack)==0:
        place.append(i)
        if i!= len(s)-1:
            place.append(i+1)


ret  = ""
for i in range(0,len(place)//2):
    ele_ = s[place[i*2]+1:place[i*2+1]]
    ret +=ele_

print(ret)