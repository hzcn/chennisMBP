count = 1
while count <= 3:
    user = input("please input username: ")
    password = input("please input password")
    if user == "alex" and password == "alex":
        print('login successful')
        break
    else:
        print('login failed %d' % count)
    if count == 3:
        choice = input('Do you want to continue? Y or N:')
        if choice == 'Y':
            count = 1
            continue
        elif choice == 'N':
            break
        else:
            print('input error')
            break
    count += 1