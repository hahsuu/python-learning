import time

print(time.clock())
print(time.altzone/3600)

print(time.asctime())
print(time.localtime())

print(time.asctime(time.localtime()))
print(time.ctime())

t_struct = time.strptime('2016/05/22', '%Y/%m/%d')
print(t_struct)

t_stamp = time.mktime(t_struct)
print(t_stamp)

print(time.strftime('%Y-%m-%d %H:%M:%S %z', time.gmtime()))