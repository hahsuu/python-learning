f = open("test.log", "w")

f.write("this is the first line\n")
f.write("this is the second line\n")


f.close()

f = open("test.log", "r")
print(f.readline())
f.close()
