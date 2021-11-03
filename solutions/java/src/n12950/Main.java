package n12950;

import java.util.Arrays;

class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int lengthY = arr1.length;
        int lengthX = arr1[0].length;
        int[][] answer = new int[lengthY][lengthX];

        for (int y = 0; y < lengthY; y++) {
            for (int x = 0; x < lengthX; x++) {
                answer[y][x] = arr1[y][x] + arr2[y][x];
            }
        }

        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        int[][] arr1 = {{1, 2}, {2, 3}};
        int[][] arr2 = {{3, 4}, {5, 6}};

        System.out.println(Arrays.deepToString(s.solution(arr1, arr2)));

        int[][] arr3 = {{1}, {2}};
        int[][] arr4 = {{3}, {4}};

        System.out.println(Arrays.deepToString(s.solution(arr3, arr4)));
    }
}
