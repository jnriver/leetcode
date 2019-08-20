#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (62.12%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    24.3K
# Total Submissions: 39K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            res = []
        elif numRows == 1:
            res = [[1]]
        elif numRows == 2:
            res = [[1], [1,1]]
        else:
            res = [[1], [1, 1]]
            for i in range(2, numRows):
                row = res[i-1]
                r1 = row[1:]
                r2 = row[:-1]
                res.append([1]+[x + y for x, y in zip(r1, r2)]+[1])
        return res

if __name__ == "__main__":
    print(Solution().generate(5))


