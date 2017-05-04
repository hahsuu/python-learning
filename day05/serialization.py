import pickle


info = {
    'alxe':'123',
    'jack':'444'
}

f = open('user.txt', 'wb')
f.write(pickle.dumps(info))
f.close()


f = open('user.txt', 'rb')
data = pickle.loads(f.read())
f.close()
for name, passwd in data.items():
    print(name, passwd)
