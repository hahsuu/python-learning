luckyNumber = 13
inputNum = int(input("请输入你的幸运数字："))
guess_count = 0
print(guess_count)

while luckyNumber != inputNum:

    if inputNum < luckyNumber:
        print("请再输入大一点的数。")

    elif inputNum > luckyNumber:
        print("请再输入小一点的数。")


    #print("****************")
    guess_count += 1
    #print(guess_count)
    if guess_count >= 3:
        break

    inputNum = int(input("请输入你的幸运数字："))
if guess_count < 3:
    print("Bingo!")
else:
    print("您已经超过！")
