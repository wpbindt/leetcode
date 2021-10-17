from collections import defaultdict

def finding_users_active_minutes(logs: List[List[int]], k: int) -> List[int]:
    user_times = defaultdict(set)
    for log_item in logs:
        user, time = log_item
        user_times[user].add(time)
    output = k * [0]
    for user, times in user_times.items():
        output[len(times) - 1] += 1
    return output

