luckyNumber = 13

while True:

    num = int(input("请输入你的幸运数字："))
    if num == luckyNumber:
        print("Bingo")
        break
    elif num < luckyNumber:
        print("请再输入大一点的数。")
    else:
        print("请再输入小一点的数。")
