def fib_memoization(n, memo):
    if n == 0 or n == 1:
        return n
    if memo[n] != None:
        return memo[n]
    memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    return memo[n]

def fib(n):
    memo = [None] * (n + 1)
    return fib_memoization(n, memo)
