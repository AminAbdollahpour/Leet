package LeetCodeProblems;

public class InegerBreakJAVA {
    public static void main(String[] args) {
        class Solution {
            public int integerBreak(int n) {
                if (n <= 1){
                    return 0;
                }
                if (n == 2) {
                    return 1;
                }
                if (n == 3) {
                    return 2;
                }
                int result = 1;
                while (n > 4) {
                    result *= n;
                    n -= 3;

                }
                return result * 3;
            }
        }
    }


}
