package n86051;

import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        return 45 - Arrays.stream(numbers).sum();
    }
}


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        int[][] numbers = {
                {1,2,3,4,6,7,8,0}, // 14
                {5,8,4,0,6,7,9}, // 6
        };

        for (int[] number: numbers) {
            System.out.println(s.solution(number));
        }
    }
}
