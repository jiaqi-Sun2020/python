"""
基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。

假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。

给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。

注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。

 

示例 1：

输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
输出：1
示例 2：

输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
输出：2
示例 3：

输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
输出：3
 

提示：

start.length == 8
end.length == 8
0 <= bank.length <= 10
bank[i].length == 8
start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-genetic-mutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# start =  "AACCGGTT"
# end   =  "AACCGGTA"
# start =  "AACCGGTT"
# end   =  "AACCGGTA"
# bank = ["AACCGGTA"]


start = "AACCGGTT"
end  = "AACCGGTA"
bank = ["AACCGGTA"]
bank1 = bank
bank2 = bank

start_list  = list(start)
end_end = list(end)

for i in range(len(end)-1,-1,-1):
    if start_list[i] != end_end[i]:
        start_list[i] = end_end[i]
        bank1 =bank1+[start]
for i in range(0,len(end)):
    if start_list[i] != end_end[i]:
        start_list[i] = end_end[i]
        bank2 =bank2+[start]
if len(bank1) and len(bank2) ==0:
    print(-1)
print(bank1)
bank1,bank2= set(bank1),set(bank2)
if len(bank1) > len(bank2):
    if start in bank2:
        print(len(bank2)-1)
    else:
        print(len(bank2))
else:
    if start in bank1:
        print(len(bank1)-1)
    else:
        print(len(bank1))




