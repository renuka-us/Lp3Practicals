import timeit
def fibonacci(n):
    """Non recursive fibonacci function"""
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    return fib_list[n]
N = int(input("Enter the value of N: "))
RUNS = 1000
print(f"Given N = {N}\n{RUNS} runs")
fib_list = [0] * (N + 1)
fib_list[0] = 0
fib_list[1] = 1
non_recursive_result = fibonacci(N)
non_recursive_time = timeit.timeit("fibonacci(N)", setup=f"from __main__ import fibonacci;N={N}", number=RUNS)
print(
f"Fibonacci non-recursive for N = {N} \tTime: {non_recursive_time:.5f} seconds O(n)\tSpace: O(1)")
# Print the Fibonacci series
print(f"Fibonacci series for N = {N}:")
for i in range(N):
    print(fib_list[i], end=" ")
print()
# Output:
# Enter the value of N: 8
# Given N = 8
# 1000 runs
# Fibonacci non-recursive for N = 8 Time: 0.00488 seconds O(n) Space: O(1)
# Fibonacci series for N = 8:
# 0 1 1 2 3 5 8 13
import timeit
def fibonacci_recursive(n):
    """Recursive fibonacci function"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_recur_list[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return fib_recur_list[n]
N = int(input("Enter the value of N: "))
RUNS = 1000
print(f"Given N = {N}\n{RUNS} runs")
fib_recur_list = [0] * (N + 1)
fib_recur_list[0] = 0
fib_recur_list[1] = 1
recursive_result = fibonacci_recursive(N)
recursive_time = timeit.timeit("fibonacci_recursive(N)", setup=f"from __main__ import fibonacci_recursive;N={N}", number=RUNS)
print(f"Fibonacci recursive for N = {N} \tTime: {recursive_time:.5f} seconds O(2^n)\tSpace: O(n)")
# Print the Fibonacci series
print(f"Fibonacci series for N = {N}:")
for i in range(N):
    print(fib_recur_list[i], end=" ")
print()
# Output:
# Enter the value of N: 8
# Given N = 8
# 1000 runs
# Fibonacci recursive for N = 8 Time: 0.02900 seconds O(2^n) Space: O(n)
# Fibonacci series for N = 8:
# 0 1 1 2 3 5 8 13