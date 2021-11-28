package n76501;

class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int result = 0;
        for (int i = 0; i < absolutes.length; i++) {
            result += absolutes[i] * boolToInt(signs[i]);
        }
        return result;
    }

    private int boolToInt(boolean sign) {
        return sign ? 1 : -1;
    }
}
