
#%%
import timeit
import matplotlib.pyplot as plt

def fibonacci_top_down(n):
    if n <= 2:
        return 1
    return fibonacci_top_down(n-1) + fibonacci_top_down(n-2)


def fibonacci_bottom_up(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]
    
    
execution_times_top_down = []
execution_times_bottom_up = []

for i in range(1, 101):
    execution_time_top_down_ = timeit.timeit(lambda: fibonacci_top_down(i), number=1)
    execution_times_top_down.append(execution_time_top_down_)

    
    print(f"Top-down: F({i}) time: {execution_time_top_down_} seconds")

    execution_time_bottom_up_ = timeit.timeit(lambda: fibonacci_bottom_up(i), number=1)
    execution_times_bottom_up.append(execution_time_bottom_up_)
    print(f"Bottom-up: F({i}) time: {execution_time_bottom_up_} seconds")
    
    if execution_time_top_down_ > 43200 or execution_time_bottom_up_ > 43200:  # If it takes more than 12 hours, stop
        max_n = i
        print(f"Execution time exceeded 12 hours for F({i}), stopping.")
        break


plt.plot(range(max_n), execution_times_top_down, label='Top-down')
plt.plot(range(max_n), execution_times_bottom_up, label='Bottom-up')
plt.title("Execution Time of Fibonacci Numbers F(1) to F(%d)" %max_n)
plt.xlabel("Fibonacci Number")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.show()
#%%

import time
import matplotlib.pyplot as plt

# Bottom-up (dynamic programming) implementation of Fibonacci function
def fibonacci_bottom_up_with_count(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    fib_4_count = 0 # Counter for F(4) computations
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        if i >= 5:
            fib_4_count += fib[i - 4] # Count F(4) computations
    return fib_4_count

# Calculate the times F(4) computed when computing F(5), F(6), ..., F(50)
fib_4_counts = []

for i in range(5, 51):
    fib_4_counts.append(fibonacci_bottom_up_with_count(i))
    print(f"F(4) computed during calculation of F({i})")

# Plot the results
plt.plot(range(5, 51), fib_4_counts)
plt.title("Count of F(4) Computed During Calculation of F(5) to F(50)")
plt.xlabel("Fibonacci Number")
plt.ylabel("Count of F(4) Computations")
plt.show()






# Global variable to count the occurrences of F(4) computations
fib_4_count = 0
fib_4_counts = []
# Top-down (pure recursive) implementation of Fibonacci function with memoization
def fibonacci_top_down_with_count(n, memo={}):
    global fib_4_count
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Check if the result is already memoized
    if n in memo:
        return memo[n]
    
    # Increment the count if computing F(4)
    if n == 4:
        fib_4_count += 1
    
    # Recursive calls to compute Fibonacci numbers
    memo[n] = fibonacci_top_down_with_count(n - 1, memo) + fibonacci_top_down_with_count(n - 2, memo)
    return memo[n]

# Example usage
for i in range(5, 51):
    fib_4_counts.append(fibonacci_top_down_with_count(i))
    print(f"F(4) computed during calculation of F({i})")

# Plot the results
plt.plot(range(5, 51), fib_4_counts)
plt.title("Count of F(4) Computed During Calculation of F(5) to F(50)")
plt.xlabel("Fibonacci Number")
plt.ylabel("Count of F(4) Computations")
plt.show()


    