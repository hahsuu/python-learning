def login(func):
    def inner(*args, **kwargs):
        print("user verfication...")
        return func(*args, **kwargs)
    return inner



def home(name):
    print("Welcome [%s] to home page" % name)

@login
def tv(name, passwd):
    print("Welcome [%s] to tv page" % name)
    print(passwd)

@login
def moive(name):
    print("Welcome [%s] to moive page" % name)

#tv=login(tv)
tv('tom', '1234')
moive('jerry')