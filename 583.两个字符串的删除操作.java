/*
 * @lc app=leetcode.cn id=583 lang=java
 *
 * [583] 两个字符串的删除操作
 *
 * https://leetcode-cn.com/problems/delete-operation-for-two-strings/description/
 *
 * algorithms
 * Medium (58.79%)
 * Likes:    275
 * Dislikes: 0
 * Total Accepted:    39.7K
 * Total Submissions: 65.4K
 * Testcase Example:  '"sea"\n"eat"'
 *
 * 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
 *
 *
 *
 * 示例：
 *
 * 输入: "sea", "eat"
 * 输出: 2
 * 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 给定单词的长度不超过500。
 * 给定单词中的字符只含有小写字母。
 *
 *
 */

// @lc code=start
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            char c1 = word1.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                char c2 = word2.charAt(j - 1);
                if (c1 == c2) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        int lcs = dp[m][n];
        return m - lcs + n - lcs;
    }
}
// @lc code=end

