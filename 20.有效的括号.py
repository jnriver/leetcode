#!/usr/bin/env python
# - * -coding: utf - 8 - * -

#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.18%)
# Total Accepted:    60.6K
# Total Submissions: 162.8K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = ['']

        for c in s:
            if c in {'(', '[', '{'}:
                l.append(c)
            elif c == '}':
                if l[-1] == '{':
                    del l[-1]
                else:
                    return False
            elif c == ']':
                if l[-1] == '[':
                    del l[-1]
                else:
                    return False
            elif c == ')':
                if l[-1] == '(':
                    del l[-1]
                else:
                    return False
        return len(l) == 1

if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()'))
