import math

def generate_execution_observation_table(input_sizes):
    # Calculate exact recursive Fibonacci function call count
    def get_fib_calls(n):
        calls = 0
        def fib(val):
            nonlocal calls
            calls += 1
            if val == 0:
                return 0
            if val == 1:
                return 1
            return fib(val - 1) + fib(val - 2)
        fib(n)
        return calls

    # Initialize output list with required table title and space-separated header row
    output = [
        "Algorithm Execution Observation Table",
        "InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort"
    ]

    # Calculate deterministic operation counts based on exact rules:
    # - Recursive Factorial: n + 1
    # - Iterative Factorial: n
    # - Recursive Fibonacci: function call count
    # - Iterative Fibonacci: n
    # - Linear Search: n
    # - Binary Search: floor(log2(n)) + 1
    # - Bubble Sort: n * (n - 1) // 2
    # - Insertion Sort: n * (n - 1) // 2
    for n in input_sizes:
        rec_fact = n + 1
        iter_fact = n
        rec_fib = get_fib_calls(n)
        iter_fib = n
        linear_search = n
        binary_search = math.floor(math.log2(n)) + 1
        bubble_sort = (n * (n - 1)) // 2
        insertion_sort = (n * (n - 1)) // 2

        # Append space-separated values for the current input size row
        row = f"{n} {rec_fact} {iter_fact} {rec_fib} {iter_fib} {linear_search} {binary_search} {bubble_sort} {insertion_sort}"
        output.append(row)

    return output