def before(request, kargs):
    print('before')


def after(request, kargs):
    print('after')


def filter_decorator(before_func, after_func):
    def decorator(func):
        def wrap(request, kargs):
            before_func(request, kargs)
            func(request, kargs)
            after_func(request, kargs)
        return wrap
    return decorator


#执行filter函数
#变成@decorator
#index变成了wrap
@filter_decorator(before, after)
def index(requst, kargs):
    print('index')

index('req', 'jerry')
