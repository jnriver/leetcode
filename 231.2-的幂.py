#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (45.74%)
# Likes:    111
# Dislikes: 0
# Total Accepted:    19.7K
# Total Submissions: 43K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例 1:
#
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
#
# 示例 2:
#
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
#
# 示例 3:
#
# 输入: 218
# 输出: false
#
#
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        elif n == 1:
            return True
        else:
            return 0 == n & (n - 1)


if __name__ == "__main__":
    print(Solution().isPowerOfTwo(1))
