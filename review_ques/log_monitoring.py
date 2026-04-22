from sympy.codegen.ast import continue_

attempts = [
    ("user1", "fail"),
    ("user2", "success"),
    ("user1", "fail"),
    ("user1", "fail"),
    ("user2", "fail")
]

trail_map = {}
for attempt in attempts:
    trail_map[attempt[0]] = trail_map.get(attempt[0], 0) + 1 if attempt[1] == "fail" else 0

safe_users = []
suspicious_users = []
for user, fails in trail_map.items():
    if trail_map.get(user) < 3:
        safe_users.append(user)
    else:
        suspicious_users.append(user)

print("Suspicious = " + ", ".join(suspicious_users))
print("Safe_users = " + ", ".join(safe_users))


