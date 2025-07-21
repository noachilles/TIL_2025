import check

users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]

if __name__ == "__main__":
    adults = list()
    active_users = list()
    active_adults = list()
    for user in users:
        if check.check_adults(user):
            adults.append(user)
        if check.check_active(user):
            active_users.append(user)
        if check.check_adults_active(user):
            active_adults.append(user)
    print(f'Adults: {adults}')
    print(f'Active Users: {active_users}')
    print(f'Active Adult Users: {active_adults}')