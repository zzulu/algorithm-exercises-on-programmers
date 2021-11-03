package n77484;

import java.util.Arrays;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int count = 0;
        int zero = 0;
        int[] rank = {6, 6, 5, 4, 3, 2, 1};

        for (Integer number: lottos) {
            if (number == 0) {
                zero += 1;
            }
            else if (Arrays.stream(win_nums).anyMatch(number::equals)) {
                count += 1;
            };
        }

        int max_rank = rank[count + zero];
        int min_rank = rank[count];

        return new int[]{max_rank, min_rank};
    }
}


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        int[] lottos1 = {44, 1, 0, 0, 31, 25};
        int[] winNums1 = {31, 10, 45, 1, 6, 19};
        System.out.println(Arrays.toString(s.solution(lottos1, winNums1)));

        int[] lottos2 = {0, 0, 0, 0, 0, 0};
        int[] winNums2 = {38, 19, 20, 40, 15, 25};
        System.out.println(Arrays.toString(s.solution(lottos2, winNums2)));

        int[] lottos3 = {45, 4, 35, 20, 3, 9};
        int[] winNums3 = {20, 9, 3, 45, 4, 35};
        System.out.println(Arrays.toString(s.solution(lottos3, winNums3)));
    }
}
