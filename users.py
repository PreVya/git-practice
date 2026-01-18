def users(user):
    roles={
        "admin": ["read", "write", "delete"],
        "guest": ["read"],
        "user": ["read", "write"]
    }

    if user in roles:
        return roles[user]
    else:
        return []