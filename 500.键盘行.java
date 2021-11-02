/*
 * @lc app=leetcode.cn id=500 lang=java
 *
 * [500] 键盘行
 *
 * https://leetcode-cn.com/problems/keyboard-row/description/
 *
 * algorithms
 * Easy (70.94%)
 * Likes:    153
 * Dislikes: 0
 * Total Accepted:    34.6K
 * Total Submissions: 48K
 * Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
 *
 * 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
 *
 * 美式键盘 中：
 *
 *
 * 第一行由字符 "qwertyuiop" 组成。
 * 第二行由字符 "asdfghjkl" 组成。
 * 第三行由字符 "zxcvbnm" 组成。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：words = ["Hello","Alaska","Dad","Peace"]
 * 输出：["Alaska","Dad"]
 *
 *
 * 示例 2：
 *
 *
 * 输入：words = ["omk"]
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：words = ["adsdf","sfd"]
 * 输出：["adsdf","sfd"]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 1
 * words[i] 由英文字母（小写和大写字母）组成
 *
 *
 */

// @lc code=start
class Solution {
    public String[] findWords(String[] words) {
        List<String> ansList = new ArrayList<String>();
        int ansIdx = 0;
        String rowIdx = "12210111011122000010020202";

        for (String w : words) {
            Boolean isSame = true;
            char row = rowIdx.charAt(Character.toLowerCase(w.charAt(0)) - 'a');
            for (int i = 0; i < w.length(); i++) {
                if (rowIdx.charAt((Character.toLowerCase(w.charAt(i))) - 'a') != row) {
                    isSame = false;
                    break;
                }
            }
            if (isSame) {
                ansList.add(w);
            }
        }
        String[] ans = new String[ansList.size()];
        for (int i = 0; i < ansList.size(); ++i) {
            ans[i] = ansList.get(i);
        }
        return ans;
    }
}
// @lc code=end

