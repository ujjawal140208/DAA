import math

def generate_runtime_complexity_table(n):
    linear_count = n
    binary_count = math.floor(math.log2(n)) + 1 if n > 0 else 0
    bubble_count = n * (n - 1) // 2
    insertion_count = n * (n - 1) // 2

    return [
        "Runtime Complexity Comparison",
        "Method ObservedCount ExpectedComplexity Observation",
        f"Linear Search {linear_count} O(n) Grows linearly",
        f"Binary Search {binary_count} O(log n) Grows logarithmically",
        f"Bubble Sort {bubble_count} O(n^2) Grows quadratically",
        f"Insertion Sort {insertion_count} O(n^2) Grows quadratically"
    ]