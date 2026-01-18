from auth import authenticate
from manage import manage
def main():
    print("This is git and github practice.")
    print("Version 1.0.0")

if __name__ =="__main__":
    main()
    users=["admin", "guest", "user"]
    user = "admin"
    login_status = authenticate(user)
    if login_status:
        print(f"User {user} authenticated successfully.")
    else:
        print(f"User {user} failed to authenticate.")
   
    for user in users:
        permissions = users(user)
        print(f"User: {user}, Permissions: {permissions}")
    
    print("The user role management system is operational.")
    print("End of the program.")
    print("Switched to main branch!")
    print("--- IGNORE ---")
    print("This is to test revert git command")
    print("Revert 0")
    print("This is new brnach features")

    print("Are you an admin?")
    if manage(user):
        print("Access granted to admin features.")
    else:
        print("Access denied. Admins only.")

    print("Will do interactive rebase and squash commits and fixuop commits")
    print("This is for interactive rebasing")
    print("Commmit A for interactive rebase")
    print("Commit B for interactive rebase")
    print("Commit C for interactive rebase")
    print("Commit D for interactive rebase")