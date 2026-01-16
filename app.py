from auth import authenticate
def main():
    print("This is git and github practice.")
    print("Version 1.0.0")

if __name__ =="__main__":
    main()
    user = "admin"
    login_status = authenticate(user)
    if login_status:
        print(f"User {user} authenticated successfully.")
    else:
        print(f"User {user} failed to authenticate.")


