'''
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

 

示例 1:

输入:
first = "pale"
second = "ple"
输出: True
 

示例 2:

输入:
first = "pales"
second = "pal"
输出: False

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/one-away-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


'''


'''
双指针模拟
为了方便，我们令 a = firsta=first、b = secondb=second，两者长度为 nn 和 mm，并让 aa 为两种中的长度较短的那个（若 bb 较短，则将两者交换）。

接下来是简单的双指针处理（使用 cntcnt 记录操作次数）：

我们最多使用不超过一次的操作，因此如果 \left | n - m \right | > 1∣n−m∣>1，直接返回 False；
若两者长度差不超过 11，使用 ii 和 jj 分别指向两字符的最左侧进行诸位检查：
若 a[i] = b[j]a[i]=b[j]，让 ii 和 jj 继续后移进行检查；
若 a[i] \neq b[j]a[i]

​
 =b[j]，根据两字符串长度进行分情况讨论：
若 n = mn=m，说明此时只能通过「替换」操作消除不同，分别让 ii 和 jj 后移，并对 cntcnt 进行加一操作；
若 n \neq mn

​
 =m，由于我们人为确保了 aa 更短，即此时是 n < mn<m，此时只能通过对 aa 字符串进行「添加」操作来消除不同，此时让 jj 后移，ii 不动（含义为在 aa 字符串中的 ii 位置增加一个 b[j]b[j] 字符），并对 cntcnt 进行加一操作。
最终我们根据 cntcnt 是否不超过 11 来返回结果。

作者：AC_OIer
链接：https://leetcode.cn/problems/one-away-lcci/solution/by-ac_oier-7ml0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


'''

'''
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if m < n:
            return self.oneEditAway(second, first)
        if m - n > 1:
            return False
        for i, (x, y) in enumerate(zip(first, second)):
            if x != y:
                return first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:]  # 注：改用下标枚举可达到 
        return True
        
'''












first = "b"
second = ""

first_l = list(first)
second_l = list(second)
number_ = 0
flag =0
if len(first_l)==len(second_l):
    if len(first_l)==0:
        print(True)
    for i,ele in enumerate(second_l):
        if first_l[i] !=ele:
            if flag==0:
                flag = 1
            if flag==1:
                print( False)

elif abs(len(first_l)-len(second_l))==1:
    for ele in second_l:
        if ele in first_l:
            number_ += 1

    if number_ ==len(second_l)-1 or number_ ==len(second_l)+1:
        print(True)
    else:
        print(False)
else:
    print(False)





