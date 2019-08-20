#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (55.94%)
# Likes:    70
# Dislikes: 0
# Total Accepted:    15.4K
# Total Submissions: 27.5K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
#
#
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
#
#
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        row = self.getRow(rowIndex-1)
        r1 = row[1:]
        r2 = row[:-1]
        return [1] + [x + y for x, y in zip(r1, r2)] + [1]


if __name__ == "__main__":
    print(Solution().getRow(3))
