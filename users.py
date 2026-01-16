def users(user):
    roles = {
        "admin":["read","write","update","delete"],
        "guest":["read"],
        "user":["login","read","write"]
    }
    if user in roles:
        return roles[user]
    else:
        return []   