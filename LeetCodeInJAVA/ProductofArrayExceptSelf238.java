package LeetCodeInJAVA;

import java.util.Arrays;

public class ProductofArrayExceptSelf238 {
    public static void main(String[] args) {
        class Solution {
            public int[] productExceptSelf(int[] nums) {
                int n = nums.length;
                int ans[] = new int[n];
                Arrays.fill(ans, 1);
                int curr = 1;
                for (int i = 0; i < n; i++) {
                    ans[i] *= curr;
                    curr *= nums[i];
                }
                curr = 1;
                for (int i = n - 1; i >= 0; i--) {
                    ans[i] *= curr;
                    curr *= nums[i];
                }
                return ans;
            }
        }
    }
}
