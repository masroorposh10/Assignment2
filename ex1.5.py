import timeit
import matplotlib.pyplot as plt
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)



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
time_org = []
time_memo = []
for i in range(0,35):
    time_org.append(timeit.timeit(lambda: func(i), number=1))
for j in range(0,35):
    time_memo.append(timeit.timeit(lambda: fib(j), number=1))


plt.plot(list(range(35)),time_org)
plt.xlabel("Numbers")
plt.ylabel("time_taken")

plt.show()
plt.plot(list(range(35)),time_memo)
plt.xlabel("Numbers")
plt.ylabel("time_taken")

plt.show()