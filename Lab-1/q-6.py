import math

def generate_runtime_chart_report(input_sizes):
    result = [
        "Runtime Comparison Chart Data",
        "InputSize LinearSearch BinarySearch BubbleSort InsertionSort"
    ]

    for n in input_sizes:
        linear = n
        binary = math.floor(math.log2(n)) + 1 if n > 0 else 0
        bubble = n * (n - 1) // 2
        insertion = n * (n - 1) // 2

        result.append(
            f"{n} {linear} {binary} {bubble} {insertion}"
        )

    result.extend([
        "Scalability Summary",
        "Algorithm Complexity Scalability",
        "Linear Search O(n) Moderate",
        "Binary Search O(log n) Excellent",
        "Bubble Sort O(n^2) Poor",
        "Insertion Sort O(n^2) Poor",
        "Key Observations",
        "Best Algorithm: Binary Search",
        "Most Expensive Algorithm: Bubble Sort",
        "Conclusion: Logarithmic algorithms scale better for large inputs"
    ])

    return result