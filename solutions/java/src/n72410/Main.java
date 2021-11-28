package n72410;

class Solution {
    public String solution(String newId) {
        String result = newId.toLowerCase()
                .replaceAll("[^a-z0-9-_.]", "")
                .replaceAll("\\.+", ".");

        if (result.startsWith(".")) {
            result = result.substring(1);
        }

        if (result.endsWith(".")) {
            result = result.substring(0, result.length()-1);
        }

        if (result.isEmpty()) {
            result = "a";
        }

        if (result.length() >= 16) {
            result = result.substring(0, 15);
            if (result.endsWith(".")) {
                result = result.substring(0, result.length()-1);
            }
        }

        if (result.length() <= 2) {
            char lastChar = result.charAt(result.length()-1);
            result = result + String.valueOf(lastChar).repeat(3 - result.length());
        }

        return result;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        String newId1 = "...!@BaT#*..y.abcdefghijklm";
        System.out.println(s.solution(newId1));

        String newId2 = "z-+.^.";
        System.out.println(s.solution(newId2));

        String newId3 = "=.=";
        System.out.println(s.solution(newId3));

        String newId4 = "123_.def";
        System.out.println(s.solution(newId4));

        String newId5 = "abcdefghijklmn.p";
        System.out.println(s.solution(newId5));
    }
}
