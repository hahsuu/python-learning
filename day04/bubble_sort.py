import random


def bubble_sort(data):
    print('before sorted!')
    print(data)
    for j in range(1, len(data)):
        for i in range(len(data)-j):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]

    print('after sorted')
    print(data)
    print('user sorted method')
    print(sorted(data))


if __name__ == '__main__':
    data = [random.randint(10, 999) for i in range(20)]
    bubble_sort(data)

