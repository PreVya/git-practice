def admin(user):
    if user == "admin":
        return "All permissions granted."
    if user=="guest":
        return "Read-only access."
    if user=="user":
        return "Read and write access."
    else:
        return "No access."