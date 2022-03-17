import task_9_3_Users
def main():
    user1 = task_9_3_Users.User('Kris','Kozak',38,'Programmer')
    user2 = task_9_3_Users.User('Jacek','Mencel',38,'Menager')
    user3 = task_9_3_Users.User('Greg','Kozok',34,'Businessman')

    user1.describe_user()
    print()
    user2.describe_user()
    print()
    user3.describe_user()
    print()
    user1.greet_user()
    user2.greet_user()
    user3.greet_user()

main()