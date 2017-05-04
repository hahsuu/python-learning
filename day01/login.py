import os

tryCount = 0
username = input("请输入用户名：")
if os.path.exists('lock.ini'):

    f = open("lock.ini", "r")
    for line in f.readlines():
        if line == username:
            print('用户已经被锁定！')
            exit(10)

success = False
while tryCount < 3:
    password = input("请输入密码：")
    tryCount += 1

    if username == 'admin' and password == 'admin':
        print('登录成功！')
        success = True
        break


if not success:
    f = open("lock.ini", "w")
    f.write(username)
    f.close()
