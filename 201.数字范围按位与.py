#
# @lc app=leetcode.cn id=201 lang=python
#
# [201] 数字范围按位与
#
# https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (39.44%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 6.3K
# Testcase Example:  '5\n7'
#
# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
#
# 示例 1: 
#
# 输入: [5,7]
# 输出: 4
#
# 示例 2:
#
# 输入: [0,1]
# 输出: 0
#
#
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while not m == n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i


