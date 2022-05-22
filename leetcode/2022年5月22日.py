"""
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和 达到或超过  100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家 不能 重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定两个整数 maxChoosableInteger （整数池中可选择的最大数）和 desiredTotal（累计和），若先出手的玩家是否能稳赢则返回 true ，否则返回 false 。假设两位玩家游戏时都表现 最佳 。

 

示例 1：

输入：maxChoosableInteger = 10, desiredTotal = 11
输出：false
解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
示例 2:

输入：maxChoosableInteger = 10, desiredTotal = 0
输出：true
示例 3:

输入：maxChoosableInteger = 10, desiredTotal = 1
输出：true
 

提示:

1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/can-i-win
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def dfs(usedNumbers: int, currentTotal: int) -> bool:
            for i in range(maxChoosableInteger):
                if (usedNumbers >> i) & 1 == 0:
                    if currentTotal + i + 1 >= desiredTotal or not dfs(usedNumbers | (1 << i), currentTotal + i + 1):
                        return True
            return False

        return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dfs(0, 0)






"""思路分析：
由题意可知规则：两名玩家轮流选择从 1 到 maxChoosableInteger 的任意整数，累计整数和，先使得累计整数和达到 desiredTotal 的玩家，即为胜者
“玩家不能重复使用整数” ，判断先出手的玩家是否能稳赢。
分类讨论情况：
定义 sum = (1+maxChoosableInteger)*maxChoosableInteger/2;

若 maxChoosableInteger >= desiredTotal，先出手的直接选择 >= desiredTotal 的数，可以稳赢；
若 sum <= desiredTotal，则都不能赢，所以先出手的不可以稳赢；
若 sum == desiredTotal，最后取数据的人赢，最后取数据的人是否是先出手者取决于 maxChoosableInteger 是奇数偶数；
若 maxChoosableInteger < desiredTotal < sum ，先出手玩家可以选择 1~maxChoosableInteger 的任意整数，那么如何选择这个数后，下一步的累计和和剩下的数是否能保证稳赢？子问题和当前问题类似，即可以用递归方法。
实现步骤：

情况1：整数池中最大值大于期望目标值
情况2：整数池中所有数字和小于期望目标值
情况3：整数池中所有数字和等于期望目标值
情况4：desiredTotal 在[最大值 , 1～maxChoosableInteger的累计和] 范围内时
遍历 1～maxChoosableInteger 的数，如果选择这个数，下一位选手不能稳赢，就说明这个数可以稳赢；
若遍历结束无论选择哪一个数下一位选手都稳赢，则当前选手必输；
递归判断下一位选手是否稳赢时，用剩下的数，和剩下的累计和来判断；
调用递归函数，返回是否可以稳赢结果。
具体代码如下：

C++

class Solution {
public:
    unordered_map<int, bool> map; //某个局面下，接下来选择数的玩家（先手）是必赢还是必输
    int maxChoosableInteger;
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        this->maxChoosableInteger = maxChoosableInteger;
        int sums = (1+maxChoosableInteger)*maxChoosableInteger/2;
        /* 情况1：整数池中最大值大于期望目标值 */
        if(maxChoosableInteger >= desiredTotal) return true;
        /* 情况2：整数池中所有数字和小于期望目标值 */
        if(sums < desiredTotal) return false;
        /* 情况3：整数池中所有数字和等于期望目标值 */
        if(sums == desiredTotal) return maxChoosableInteger&1 == 1;
        /* 情况4：desiredTotal 在 [ maxChoosableInteger , 1-maxChoosableInteger 的累计和 ] 范围内时 */
        return dfs(0, desiredTotal);
    }
    bool dfs(int state, int leftTotal) {
            if(map.count(state) != 0) return map[state];
            for(int number = maxChoosableInteger; number >= 1; number--) {
                int number_bit = 1 << (number - 1);
                if (state & number_bit) continue;
                if (number >= leftTotal || !dfs(state | number_bit, leftTotal - number)) {
                    /* 选这个数就马上赢，或者选了之后对方接下来必输 */
                    map[state] = true;
                    /* 那当前玩家选这个数就好了，必赢 */
                    return true;
                }
            }
            map[state] = false;
            /* 没有一种选择可赢，那么必输 */
            return false;
    }
};
复杂度分析:

时间复杂度：O(2^n2
n
 ×n)，其中 n = maxChoosableInteger;
空间复杂度：O(2^n2
n
 )。

作者：Nehzil
链接：https://leetcode.cn/problems/can-i-win/solution/by-nehzil-icsu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""