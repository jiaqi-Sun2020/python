"""
给你一个日志数组 logs。每条日志都是以空格分隔的字串，其第一个字为字母与数字混合的 标识符 。

有两种不同类型的日志：

字母日志：除标识符之外，所有字均由小写字母组成
数字日志：除标识符之外，所有字均由数字组成
请按下述规则将日志重新排序：

所有 字母日志 都排在 数字日志 之前。
字母日志 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序。
数字日志 应该保留原来的相对顺序。
返回日志的最终顺序。

 

示例 1：

输入：logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
输出：["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
解释：
字母日志的内容都不同，所以顺序为 "art can", "art zero", "own kit dig" 。
数字日志保留原来的相对顺序 "dig1 8 1 5 1", "dig2 3 6" 。
示例 2：

输入：logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

提示：

1 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] 中，字与字之间都用 单个 空格分隔
题目数据保证 logs[i] 都有一个标识符，并且在标识符之后至少存在一个字

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-data-in-log-files
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""
logs =  ["dig1 8 1 5 1","let1 art can","aet2 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Digitals = []
Alphas = []
for log in logs:
    if log[-1].isdigit():
        Digitals.append(log)
    elif log[-1].isalpha():
        Alphas.append(log)
Alphas.sort(key=lambda x: x.split(" ")[0])
Alphas.sort(key=lambda x: x.split(" ")[1:])
print(Digitals)
print("="*20)
print(Alphas)


print(Alphas + Digitals)


"""
方法一：自定义排序
思路

根据题意自定义排序的比较方式。比较时，先将数组日志按照第一个空格分成两部分字符串，其中第一部分为标识符。第二部分的首字符可以用来判断该日志的类型。两条日志进行比较时，需要先确定待比较的日志的类型，然后按照以下规则进行比较：

字母日志始终小于数字日志。
数字日志保留原来的相对顺序。当使用稳定的排序算法时，可以认为所有数字日志大小一样。当使用不稳定的排序算法时，可以用日志在原数组中的下标进行比较。
字母日志进行相互比较时，先比较第二部分的大小；如果相等，则比较标识符大小。比较时都使用字符串的比较方式进行比较。
定义比较函数 \textit{logCompare}logCompare 时，有两个输入 \textit{log}_1log 
1
​
  和 \textit{log}_2log 
2
​
  。当相等时，返回 00；当 \textit{log}_1log 
1
​
  大时，返回正数；当 \textit{log}_2log 
2
​
  大时，返回负数。

代码

Python3JavaC#C++CJavaScriptGolang

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log: str) -> tuple:
            a, b = log.split(' ', 1)
            return (0, b, a) if b[0].isalpha() else (1,)

        logs.sort(key=trans)  # sort 是稳定排序    在这个地方它每次都是根据key做了判断出来的
        return logs
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 是 \textit{logs}logs 的字符数，是平均情况下内置排序的时间复杂度。

空间复杂度：O(n)O(n) 或 O(1)O(1)（取决于语言实现）。需要新建数组保存 \textit{log}log 和下标，需要将每条 \textit{log}log 进行拆分。

"""