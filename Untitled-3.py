fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Generate Fibonacci series with 50 elements
fib_series = [fibonacci(i) for i in range(50)]

print(fib_series)