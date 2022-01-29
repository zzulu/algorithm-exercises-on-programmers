package n92334;

import java.util.*;
import java.util.stream.Collectors;

public class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        List<String> reports =  Arrays.stream(report).distinct().collect(Collectors.toList());
        Map<String, Integer> reportedUsers = new HashMap<>();
        Map<String, Integer> mailUsers = new LinkedHashMap<>();

        for (String user: id_list) {
            reportedUsers.put(user, 0);
            mailUsers.put(user, 0);
        }

        for (String r: reports) {
            String userReported = r.split(" ")[1];
            reportedUsers.put(userReported, reportedUsers.get(userReported) + 1);
        }

        for (String r: reports) {
            String userReport = r.split(" ")[0];
            String userReported = r.split(" ")[1];
            if (reportedUsers.get(userReported) >= k) {
                mailUsers.put(userReport, mailUsers.get(userReport) + 1);
            }
        }

        return mailUsers.values().stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        String[] id_list1 = {"muzi", "frodo", "apeach", "neo"};
        String[] report1 = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
        int k1 = 2;

        System.out.println(Arrays.toString(s.solution(id_list1, report1, k1)));

        String[] id_list2 = {"con", "ryan"};
        String[] report2 = {"ryan con", "ryan con", "ryan con", "ryan con"};
        int k2 = 3;

        System.out.println(Arrays.toString(s.solution(id_list2, report2, k2)));
    }
}
