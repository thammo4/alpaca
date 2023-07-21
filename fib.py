def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci_recursive(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

a = fibonacci_recursive(10);

print('fib seq of first ten nums 10 = {}'.format(a));