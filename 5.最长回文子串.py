#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.21%)
# Likes:    886
# Dislikes: 0
# Total Accepted:    60.5K
# Total Submissions: 239.8K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
#
#
class Solution(object):
    def isPalindrome(self,s):
        s == s[::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = i = 0
        string = ""
        while i < len(s):
            if self.isPalindrome(s[start:i]):
                pass
            else:
                pass



