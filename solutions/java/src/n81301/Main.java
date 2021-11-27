package n81301;

class Solution {
    public Integer solution(String s) {
        String[] numbers = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

        for (int i = 0; i < numbers.length; i++) {
            s = s.replaceAll(numbers[i], Integer.toString(i));
        }

        return Integer.parseInt(s);
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        String s1 = "one4seveneight";
        System.out.println(solution.solution(s1));

        String s2 = "23four5six7";
        System.out.println(solution.solution(s2));

        String s3 = "2three45sixseven";
        System.out.println(solution.solution(s3));

        String s4 = "123";
        System.out.println(solution.solution(s4));
    }
}
