"""
给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。

 

示例 1:

输入：n = 2
输出：987
解释：99 x 91 = 9009, 9009 % 1337 = 987
示例 2:

输入： n = 1
输出： 9
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-palindrome-product
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



# print(huiwen(5005))





def largestPalindrome(n: int) -> int:
    # 判断回文数
    def huiwen(number):
        num = list(str(number))
        str_size = len(num)
        #print(str_size)
        for i in range(int(str_size / 2)):  # 向下取整的
            if num[i] != num[-i - 1]:
                return False
        return True
    max_num = 0
    if n==1:
        return 9
    min  = 10**(n-1)
    max  = 10**(n)
    print(min,max)
    for i in range(min,max):
        for j in range(min,max):
            if huiwen(i*j) and i*j>max_num:
                print(huiwen(i * j))
                max_num = i*j
                print(i,j)
    return max_num%1337


# def largestPalindrome(n: int) -> int:
#     # 判断回文数
#     def huiwen(number):
#         num = list(str(number))
#         str_size = len(num)
#         #print(str_size)
#         for i in range(int(str_size / 2)):  # 向下取整的
#             if num[i] != num[-i - 1]:
#                 return False
#         return True
#     max_num = 0
#     if n==1:
#         return 9
#     min  = 10**(n-1)
#     max  = 10**(n)
#     print(min,max)
#     for left in range(min,max):
#         p, x = left, left
#         while x:
#             p = p * 10 + x % 10  # 翻转左半部分到其自身末尾，构造回文数 p
#             x //= 10
#         print(p)
#     return max_num



print(largestPalindrome(3))

# print(list(range(999,99,-1)))

# def huiwen(number):
#     num = list(str(number))
#     str_size = len(num)
#     #print(str_size)
#     for i in range(int(str_size / 2)):  # 向下取整的
#         if num[i] != num[-i - 1]:
#             return False
#     return True
# print(957*123)
# print(huiwen(123*957))