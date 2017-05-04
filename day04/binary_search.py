import random

data = list()
for i in range(100):
    data.append(random.randint(1, 200))

#num = data[3]
#print(num)
data = set(data)
data = list(data)
data.sort()
print(data)
#print(len(data))


def search(data, num):
    length = len(data)
    mid = length // 2
    if len(data) >= 1:
        if num == data[mid]:
            print('find %s' % data[mid])
            #return mid
        elif num < data[mid]:
            print('find in left')
            search(data[:mid], num)
        else:
            print('find in right')
            search(data[mid:], num)
    else:
        print('not find')

def binary_search(data_source, find_n):
    mid = int(len(data_source) / 2)
    if len(data_source) >= 1:
        if data_source[mid] > find_n:
            print("data in left of [%s]" % data_source[mid])
            binary_search(data_source[:mid], find_n)
        elif data_source[mid] < find_n:
            print("data in right of [%s]" % data_source[mid])
            binary_search(data_source[mid:], find_n)
        else:
            print("found find_s,", data_source)
    else:
        print("cannot find.....")



#binary_search(data, random.randint(1,200))


def binary_search_no_recursiv(data, find):
    print('find:%s' % find)
    low = 0
    high = len(data) - 1


    while low < high:
        mid = (low + high) // 2
        if find > data[mid]:#right
            #print('right')
            low = mid+1
        elif find < data[mid]:
            #print('left')
            high = mid-1
        else:
            return data[mid]
    return -1

print(binary_search_no_recursiv(data, random.randint(1,200)))