#
# @lc app=leetcode.cn id=187 lang=python
#
# [187] 重复的DNA序列
#
# https://leetcode-cn.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (42.02%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    3.1K
# Total Submissions: 7.4K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA
# 中的重复序列有时会对研究非常有帮助。
# 
# 编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。
# 
# 示例:
# 
# 输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 
# 输出: ["AAAAACCCCC", "CCCCCAAAAA"]
# 
#
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        

