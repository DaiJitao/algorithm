from typing import List, Optional


"""
import java.util.*;

public class Solution {
    public int getLongestPalindrome(String A, int n) {
        if(n < 2) {
            return n;
        }
        // 最大长度
        int res = 0; 
        // 每个字符都可以尝试作为中心点
        for(int i = 0; i < n; i++) {
            // 两种情况：可能是类似 aba 的字符串，也可能是类似 abba 的情况
            // 只需要分别计算出以一个和两个字符作为中心点的子串，取出较大的长度即可
            int len = helper(A, i, i) > helper(A, i, i+1) ? helper(A, i, i) : helper(A, i, i + 1);
            // 更新最大长度
            res = Math.max(res, len);
        }
        return res;
    }

    public int helper(String A, int left, int right) {
        // 从left到right开始向两边扩散、比较
        while(left >= 0 && right < A.length()) {
            // 如果相等则继续扩散比较
            if(A.charAt(left) == A.charAt(right)) {
                left--;
                right++;
                continue;
            }
            // 如果不相等则剪枝，不用再继续扩散比较
            break;
        }
        // "+1"是因为通过下标计算子串长度
        // "-2"是因为上边的while循环是当索引为left和right不想等才退出循环的
        // 因此此时的left和right是不满足的，需要舍弃
        return right - left + 1 - 2;

    }
}
"""