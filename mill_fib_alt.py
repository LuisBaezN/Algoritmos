from numpy import matrix

def fib(n):
    return (matrix(
        '0 1; 1 1' if n >= 0 else '-1 1; 1 0', object
        ) ** abs(n))[0, 1]

if __name__ == '__main__':
    n = 2_000_000
    fib(n)