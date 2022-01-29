def solution(id_list, report, k):
    report = set(report)
    reported_users = {user: 0 for user in id_list}
    report_users = {user: 0 for user in id_list}

    for r in report:
        reported_users[r.split(" ")[1]] += 1

    for r in report:
        if reported_users[r.split(" ")[1]] >= k:
            report_users[r.split(" ")[0]] += 1

    return list(report_users.values())


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)) #=> [2, 1, 1, 0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)) #=> [0, 0]
