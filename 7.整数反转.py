#!/usr/bin/env python
# - * -coding: utf - 8 - * -

#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (32.20%)
# Total Accepted:    105K
# Total Submissions: 326.1K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#
#
# 示例 2:
#
# 输入: -123
# 输出: -321
#
#
# 示例 3:
#
# 输入: 120
# 输出: 21
#
#
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
#
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        symbol = cmp(x, 0)
        r = symbol*int(str(x*symbol)[::-1])
        return 0 if r > 2147483647 or r < -2147483648 else r

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))

