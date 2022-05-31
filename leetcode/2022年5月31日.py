"""
现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。

给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。

请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。

字符串 s 字典顺序小于 字符串 t 有两种情况：

在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。
 

示例 1：

输入：words = ["wrt","wrf","er","ett","rftt"]
输出："wertf"
示例 2：

输入：words = ["z","x"]
输出："zx"
示例 3：

输入：words = ["z","x","z"]
输出：""
解释：不存在合法字母顺序，因此返回 "" 。
 

提示：

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/Jf1JuT
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(list)
        inDeg = {c: 0 for c in words[0]}
        for s, t in pairwise(words):
            for c in t:
                inDeg.setdefault(c, 0)
            for u, v in zip(s, t):
                if u != v:
                    g[u].append(v)
                    inDeg[v] += 1
                    break
            else:
                if len(s) > len(t):
                    return ""

        q = [u for u, d in inDeg.items() if d == 0]
        for u in q:
            for v in g[u]:
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    q.append(v)
        return ''.join(q) if len(q) == len(inDeg) else ""

























"""
前言
这道题是拓扑排序问题。外星文字典中的字母和字母顺序可以看成有向图，字典顺序即为所有字母的一种排列，满足每一条有向边的起点字母和终点字母的顺序都和这两个字母在排列中的顺序相同，该排列即为有向图的拓扑排序。

只有当有向图中无环时，才有拓扑排序，且拓扑排序可能不止一种。如果有向图中有环，则环内的字母不存在符合要求的排列，因此没有拓扑排序。

使用拓扑排序求解时，将外星文字典中的每个字母看成一个节点，将字母之间的顺序关系看成有向边。对于外星文字典中的两个相邻单词，同时从左到右遍历，当遇到第一个不相同的字母时，该位置的两个字母之间即存在顺序关系。

以下两种情况不存在合法字母顺序：

字母之间的顺序关系存在由至少 22 个字母组成的环，例如 \textit{words} = [\text{``a"}, \text{``b"}, \text{``a"}]words=[“a",“b",“a"]；

相邻两个单词满足后面的单词是前面的单词的前缀，且后面的单词的长度小于前面的单词的长度，例如 \textit{words} = [\text{``ab"}, \text{``a"}]words=[“ab",“a"]。

其余情况下都存在合法字母顺序，可以使用拓扑排序得到字典顺序。

拓扑排序可以使用深度优先搜索或广度优先搜索实现，以下分别介绍两种实现方法。

方法一：拓扑排序 + 深度优先搜索
使用深度优先搜索实现拓扑排序的总体思想是：对于一个特定节点，如果该节点的所有相邻节点都已经搜索完成，则该节点也会变成已经搜索完成的节点，在拓扑排序中，该节点位于其所有相邻节点的前面。一个节点的相邻节点指的是从该节点出发通过一条有向边可以到达的节点。

由于拓扑排序的顺序和搜索完成的顺序相反，因此需要使用一个栈存储所有已经搜索完成的节点。深度优先搜索的过程中需要维护每个节点的状态，每个节点的状态可能有三种情况：「未访问」、「访问中」和「已访问」。初始时，所有节点的状态都是「未访问」。

每一轮搜索时，任意选取一个「未访问」的节点 uu，从节点 uu 开始深度优先搜索。将节点 uu 的状态更新为「访问中」，对于每个与节点 uu 相邻的节点 vv，判断节点 vv 的状态，执行如下操作：

如果节点 vv 的状态是「未访问」，则继续搜索节点 vv；

如果节点 vv 的状态是「访问中」，则找到有向图中的环，因此不存在拓扑排序；

如果节点 vv 的状态是「已访问」，则节点 vv 已经搜索完成并入栈，节点 uu 尚未入栈，因此节点 uu 的拓扑顺序一定在节点 vv 的前面，不需要执行任何操作。

当节点 uu 的所有相邻节点的状态都是「已访问」时，将节点 uu 的状态更新为「已访问」，并将节点 uu 入栈。

当所有节点都访问结束之后，如果没有找到有向图中的环，则存在拓扑排序，所有节点从栈顶到栈底的顺序即为拓扑排序。

实现方面，由于每个节点是一个字母，因此可以使用字符数组代替栈，当节点入栈时，在字符数组中按照从后往前的顺序依次填入每个字母。当所有节点都访问结束之后，将字符数组转成字符串，即为字典顺序。


1 / 11

Python3JavaC#C++CJavaScriptGolang

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = {}
        for c in words[0]:
            g[c] = []
        for s, t in pairwise(words):
            for c in t:
                g.setdefault(c, [])
            for u, v in zip(s, t):
                if u != v:
                    g[u].append(v)
                    break
            else:
                if len(s) > len(t):
                    return ""

        VISITING, VISITED = 1, 2
        states = {}
        order = []
        def dfs(u: str) -> bool:
            states[u] = VISITING
            for v in g[u]:
                if v not in states:
                    if not dfs(v):
                        return False
                elif states[v] == VISITING:
                    return False
            order.append(u)
            states[u] = VISITED
            return True

        return ''.join(reversed(order)) if all(dfs(u) for u in g if u not in states) else ""
复杂度分析

时间复杂度：O(n \times L + |\Sigma|)O(n×L+∣Σ∣)，其中 nn 是数组 \textit{words}words 的长度，即字典中的单词数，LL 是字典中的平均单词长度，\SigmaΣ 是字典中的字母集合。遍历字典构造有向图需要 O(n \times L)O(n×L) 的时间，由于有向图包含最多 n - 1n−1 条边和 |\Sigma|∣Σ∣ 个节点，因此深度优先搜索需要 O(n + |\Sigma|)O(n+∣Σ∣) 的时间，总时间复杂度是 O(n \times L + n + |\Sigma|) = O(n \times L + |\Sigma|)O(n×L+n+∣Σ∣)=O(n×L+∣Σ∣)。

空间复杂度：O(n + |\Sigma|)O(n+∣Σ∣)，其中 nn 是数组 \textit{words}words 的长度，即字典中的单词数，\SigmaΣ 是字典中的字母集合。空间复杂度主要取决于存储有向图需要的空间，有向图包含最多 n - 1n−1 条边和 |\Sigma|∣Σ∣ 个节点。

方法二：拓扑排序 + 广度优先搜索
方法一使用深度优先搜索实现拓扑排序，根据每个节点搜索完成的顺序反向得到拓扑排序。使用广度优先搜索实现拓扑排序，则可以正向得到拓扑排序。

首先计算每个节点的入度，只有入度为 00 的节点可能是拓扑排序中最前面的节点。当一个节点加入拓扑排序之后，该节点的所有相邻节点的入度都减 11，表示相邻节点少了一条入边。当一个节点的入度变成 00，则该节点前面的节点都已经加入拓扑排序，该节点也可以加入拓扑排序。

具体做法是，使用队列存储可以加入拓扑排序的节点，初始时将所有入度为 00 的节点入队列。每次将一个节点出队列并加入拓扑排序中，然后将该节点的所有相邻节点的入度都减 11，如果一个相邻节点的入度变成 00，则将该相邻节点入队列。重复上述操作，直到队列为空时，广度优先搜索结束。

如果有向图中无环，则每个节点都将加入拓扑排序，因此拓扑排序的长度等于字典中的字母个数。如果有向图中有环，则环中的节点不会加入拓扑排序，因此拓扑排序的长度小于字典中的字母个数。广度优先搜索结束时，判断拓扑排序的长度是否等于字典中的字母个数，即可判断有向图中是否有环。

如果拓扑排序的长度等于字典中的字母个数，则拓扑排序包含字典中的所有字母，返回拓扑排序；

如果拓扑排序的长度小于字典中的字母个数，则有向图中有环，不存在拓扑排序。


1 / 12

Python3JavaC#C++CJavaScriptGolang

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(list)
        inDeg = {c: 0 for c in words[0]}
        for s, t in pairwise(words):
            for c in t:
                inDeg.setdefault(c, 0)
            for u, v in zip(s, t):
                if u != v:
                    g[u].append(v)
                    inDeg[v] += 1
                    break
            else:
                if len(s) > len(t):
                    return ""

        q = [u for u, d in inDeg.items() if d == 0]
        for u in q:
            for v in g[u]:
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    q.append(v)
        return ''.join(q) if len(q) == len(inDeg) else ""
复杂度分析

时间复杂度：O(n \times L + |\Sigma|)O(n×L+∣Σ∣)，其中 nn 是数组 \textit{words}words 的长度，即字典中的单词数，LL 是字典中的平均单词长度，\SigmaΣ 是字典中的字母集合。遍历字典构造有向图需要 O(n \times L)O(n×L) 的时间，由于有向图包含最多 n - 1n−1 条边和 |\Sigma|∣Σ∣ 个节点，因此广度优先搜索需要 O(n + |\Sigma|)O(n+∣Σ∣) 的时间，总时间复杂度是 O(n \times L + n + |\Sigma|) = O(n \times L + |\Sigma|)O(n×L+n+∣Σ∣)=O(n×L+∣Σ∣)。

空间复杂度：O(n + |\Sigma|)O(n+∣Σ∣)，其中 nn 是数组 \textit{words}words 的长度，即字典中的单词数，\SigmaΣ 是字典中的字母集合。空间复杂度主要取决于存储有向图需要的空间，有向图包含最多 n - 1n−1 条边和 |\Sigma|∣Σ∣ 个节点。

下一篇：[Python/Java/TypeScript/Go] 拓扑


作者：LeetCode-Solution
链接：https://leetcode.cn/problems/Jf1JuT/solution/wai-xing-wen-zi-dian-by-leetcode-solutio-to66/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""