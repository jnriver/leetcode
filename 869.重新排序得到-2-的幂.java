/*
 * @lc app=leetcode.cn id=869 lang=java
 *
 * [869] 重新排序得到 2 的幂
 *
 * https://leetcode-cn.com/problems/reordered-power-of-2/description/
 *
 * algorithms
 * Medium (55.14%)
 * Likes:    51
 * Dislikes: 0
 * Total Accepted:    7.2K
 * Total Submissions: 12.7K
 * Testcase Example:  '1'
 *
 * 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
 *
 * 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：1
 * 输出：true
 *
 *
 * 示例 2：
 *
 * 输入：10
 * 输出：false
 *
 *
 * 示例 3：
 *
 * 输入：16
 * 输出：true
 *
 *
 * 示例 4：
 *
 * 输入：24
 * 输出：false
 *
 *
 * 示例 5：
 *
 * 输入：46
 * 输出：true
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= N <= 10^9
 *
 *
 */

// @lc code=start
class Solution {
    public boolean reorderedPowerOf2(int n) {

    }

    public boolean isPow2(int n) {
        return (n & (n - 1)) == 0;
    }
}
// @lc code=end

