#!/usr/bin/env python
# - * -coding: utf - 8 - * -

#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.58%)
# Total Accepted:    66.3K
# Total Submissions: 203.2K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sz, ret = zip(*strs), ""
        for c in sz:
            if len(set(c)) > 1:
                break
            ret += c[0]
        return ret


if __name__ == '__main__':
    s=Solution()
    print(s.longestCommonPrefix([""]))
