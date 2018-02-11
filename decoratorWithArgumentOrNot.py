import functools

def log(textOrFunc):
    '''
    @log decorator with support of @log and @log('Execute..........')
    '''
    if isinstance(textOrFunc, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print('{} {}'.format(textOrFunc, func.__name__))
                return func(*args, **kwargs)
            return wrapper
        return decorator
    else:
        @functools.wraps(textOrFunc)
        def wrapper(*args, **kwargs):
            print('{}'.format(textOrFunc.__name__))
            return textOrFunc(*args, **kwargs)
        return wrapper

@log
def now():
    print('2018-02-11')


@log('Execute..........')
def now2():
    print('2018-02-11')

if __name__ == '__main__':
    now()
    now2()
