def fib(n, v=False):
    if v:
        import sys
        sys.set_int_max_str_digits(700_000)

    if n < 0 :
        if n % 2 == 0:
            return -fib_iter(1, 0, 0, 1, -n)
        return fib_iter(1, 0, 0, 1, -n)
    return fib_iter(1, 0, 0, 1, n)

def fib_iter(a, b, p, q, count):
    if count == 0:
        return b
    else:
        if count % 2 == 0:
            count /= 2
            count = int(count)
            p, q = p**2 + q**2, q*(q + 2*p)
            return fib_iter(a, b, p, q, count)
        else:
            a, b = (b + a)*q + a*p, b*p + a*q
            count -= 1
            return fib_iter(a, b, p, q, count)

if __name__ == '__main__':
    n = 2_000_000
    fib(n)