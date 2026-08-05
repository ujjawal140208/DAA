def analyze_recursive_iterative(n):

    # Recursive Factorial
    def rec_fact(x):
        if x == 0 or x == 1:
            return 1
        return x * rec_fact(x - 1)

    # Iterative Factorial
    def itr_fact(x):
        fact = 1
        for i in range(1, x + 1):
            fact *= i
        return fact

    # Recursive Fibonacci with call counter
    fib_calls = 0

    def rec_fib(x):
        nonlocal fib_calls
        fib_calls += 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        return rec_fib(x - 1) + rec_fib(x - 2)

    # Iterative Fibonacci
    def itr_fib(x):
        if x == 0:
            return 0
        if x == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, x + 1):
            a, b = b, a + b
        return b

    # Calculate values
    recursive_factorial = rec_fact(n)
    iterative_factorial = itr_fact(n)

    recursive_fibonacci = rec_fib(n)
    recursive_fibonacci_count = fib_calls

    iterative_fibonacci = itr_fib(n)

    # Operation counts
    recursive_factorial_count = n + 1
    iterative_factorial_count = n
    iterative_fibonacci_count = n

    return [
        "Computation Analysis Report",
        f"Recursive Factorial: {recursive_factorial}",
        f"Iterative Factorial: {iterative_factorial}",
        f"Recursive Fibonacci: {recursive_fibonacci}",
        f"Iterative Fibonacci: {iterative_fibonacci}",
        "Operation Count Comparison",
        f"Recursive Factorial Count: {recursive_factorial_count}",
        f"Iterative Factorial Count: {iterative_factorial_count}",
        f"Recursive Fibonacci Count: {recursive_fibonacci_count}",
        f"Iterative Fibonacci Count: {iterative_fibonacci_count}"
    ]
    
print(analyze_recursive_iterative(5))