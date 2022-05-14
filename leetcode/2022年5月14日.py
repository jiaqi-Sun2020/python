"""
我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。

您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。

返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。

注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。

 

示例 1：

输入： stickers = ["with","example","science"], target = "thehat"
输出：3
解释：
我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
此外，这是形成目标字符串所需的最小贴纸数量。
示例 2:

输入：stickers = ["notice","possible"], target = "basicbasic"
输出：-1
解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。
 

提示:

n == stickers.length
1 <= n <= 50
1 <= stickers[i].length <= 10
1 <= target <= 15
stickers[i] 和 target 由小写英文单词组成
通过次数7,409提交次数14,298

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/stickers-to-spell-word
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



'''
思路

记 \textit{target}target 的长度为 mm，它一共有 2^m2 
m
  个子序列（包括空子序列和 \textit{target}target 本身，字符相同但组成的下标不同的子序列视为不同的子序列）。根据动态规划的思路，拼出某个子序列 \textit{mask}mask 所需要的最小贴纸数又可以由 \textit{mask}mask 的子序列来计算，下一段介绍动态规划的思路。

在本题中，定义函数 \textit{dp}(\textit{mask})dp(mask) 来求解不同状态的最小贴纸数，输入是某个子序列 \textit{mask}mask，输出是拼出该子序列的最小贴纸数。计算拼出 \textit{mask}mask 所需的最小贴纸数时，需要选取最优的 \textit{sticker}sticker 让其贡献部分字符，未被 \textit{sticker}sticker 覆盖的其他字符 \textit{left}left 需要用动态规划继续计算。在选取最优的 \textit{sticker}sticker 时，需要遍历所有 \textit{sticker}sticker。遍历到某个 \textit{sticker}sticker 时，计算 \textit{mask}mask 和 \textit{sticker}sticker 字符的最大交集（非空），\textit{mask}mask 中这部分交集由 \textit{sticker}sticker 贡献，剩余部分的最小贴纸数由动态规划继续计算，而 \textit{sticker}sticker 中不属于最大交集的剩下部分会被舍弃，不会产生任何贡献。遍历完所有 \textit{sticker}sticker 后，选取出所有贴纸数的最小值作为本次规划的结果，这一遍历 \textit{stickers}stickers 并根据剩余部分的最小贴纸数来计算当前 \textit{mask}mask 的最小贴纸数的步骤完成了状态转移。边界情况是，如果 \textit{mask}mask 为空集，则贴纸数为 00。

在动态规划时，子序列可以用一个二进制数来表示。从低位到高位，某位为 00 则表示在 \textit{target}target 中这一位不选取，为 11 则表示选取这一位，从而完成状态压缩的过程。代码实现上，本题解选择了记忆化搜索的方式。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/stickers-to-spell-word/solution/tie-zhi-pin-ci-by-leetcode-solution-9g3z/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(target)
        @cache
        def dp(mask: int) -> int:
            if mask == 0:
                return 0
            res = m + 1
            for sticker in stickers:
                left = mask
                cnt = Counter(sticker)
                for i, c in enumerate(target):
                    if mask >> i & 1 and cnt[c]:
                        cnt[c] -= 1
                        left ^= 1 << i
                if left < mask:
                    res = min(res, dp(left) + 1)
            return res
        res = dp((1 << m) - 1)
        return res if res <= m else -1
复杂度分析

时间复杂度：O(2 ^ m \times n \times (c + m))O(2 
m
 ×n×(c+m))，其中 mm 为 \textit{target}target 的长度，cc 为每个 \textit{sticker}sticker 的平均字符数。一共有 O(2 ^ m)O(2 
m
 ) 个状态。计算每个状态时，需要遍历 nn 个 \textit{sticker}sticker。遍历每个 \textit{sticker}sticker 时，需要遍历它所有字符和 \textit{target}target 所有字符。

空间复杂度：O(2 ^ m)O(2 
m
 )，记忆化时需要保存每个状态的贴纸数量。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/stickers-to-spell-word/solution/tie-zhi-pin-ci-by-leetcode-solution-9g3z/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''