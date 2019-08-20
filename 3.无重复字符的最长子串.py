#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.47%)
# Likes:    1827
# Dislikes: 0
# Total Accepted:    125.2K
# Total Submissions: 425K
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ""
        start = maxl = 0
        i = 0
        while i < len(s):
            if s[i] not in sub:
                sub+=s[i]
                maxl = max(maxl, len(sub))
            else:
                i = start + sub.index(s[i]) + 1
                start = i
                sub = s[i]
            i += 1

        return maxl


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("aab"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
