package n76501;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] absolutes1 = {4, 7, 12};
        boolean[] signs1 = {true, false, true};
        System.out.println(solution.solution(absolutes1, signs1));

        int[] absolutes2 = {1, 2, 3};
        boolean[] signs2 = {false, false, true};
        System.out.println(solution.solution(absolutes2, signs2));
    }
}

