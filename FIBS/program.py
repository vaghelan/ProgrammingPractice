def getNthFib(n):
    # Write your code here.

    n = n - 1
    fibs = [0, 1]

    if n <= 1:
        return fibs[n]

    k = 0

    for i in range(2, n+1):
        fibs[k] = fibs[k] + fibs[k - 1]
        k = k ^ 1
    k = k ^ 1
    return fibs[k]
