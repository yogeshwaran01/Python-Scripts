from instagramy import check_username

if __name__ == "__main__":
    username = input("Enter the Username: ")
    if check_username(username):
        print("Username Found in Instagram")
    else:
        print("Username not Found")
