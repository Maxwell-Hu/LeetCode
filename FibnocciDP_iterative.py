def fib(n):
    if n < 2 : return n
    last, now =0,1
    for i in range(n-1): last,now = now, last+now
    return now
