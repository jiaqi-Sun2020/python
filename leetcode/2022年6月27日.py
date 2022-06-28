# 给定字符串列表 strs ，返回其中 最长的特殊序列 。如果最长特殊序列不存在，返回 -1 。
#
# 特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。
#
#  s 的 子序列可以通过删去字符串 s 中的某些字符实现。
#
# 例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-uncommon-subsequence-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#
#


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(s: str, t: str) -> bool:
            pt_s = pt_t = 0
            while pt_s < len(s) and pt_t < len(t):
                if s[pt_s] == t[pt_t]:
                    pt_s += 1
                pt_t += 1
            return pt_s == len(s)

        ans = -1
        for i, s in enumerate(strs):
            check = True
            for j, t in enumerate(strs):
                if i != j and is_subseq(s, t):
                    check = False
                    break
            if check:
                ans = max(ans, len(s))

        return ans



