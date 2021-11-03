package n12943;


class Solution {
    public int solution(int num) {
        long n = num;
        for (int i = 0; i < 500; i++) {
            if (n == 1) {
                return i;
            }
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = (n * 3) + 1;
            }
        }
        return -1;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        int n1 = 6;
        System.out.println(s.solution(n1));

        int n2 = 16;
        System.out.println(s.solution(n2));

        int n3 = 626331;
        System.out.println(s.solution(n3));
    }
}

