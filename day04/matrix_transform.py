import random
m = [[random.randint(10, 99) for col in range(5)] for row in range(5)]
print('转置之前：\n')
for row in m:
    print(row)
n = list(list(row) for row in zip(*m))
print('转置之后：\n')
for row in n:
    print(row)


print('只能转置方阵'.center(80, '*'))

for row_num, row in enumerate(m):
    for col_num, element in enumerate(row):
        #print(row_num, col_num, element)
        if row_num < col_num:
            m[row_num][col_num], m[col_num][row_num] = m[col_num][row_num], m[row_num][col_num]
for row in m:
    print(row)

print('end'.center(80,'*'))
