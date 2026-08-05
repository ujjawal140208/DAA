# Design and Analysis of Algorithms (DAA) - Lab & Assignment Solutions 🚀

Welcome to the **DAA (Design and Analysis of Algorithms)** repository! This repository contains a comprehensive collection of code implementations, problem statements, and algorithmic analysis for assignments and lab sessions covered during the DAA course.

---

## 📌 Overview

This repository is organized to help students and developers understand, implement, and analyze core computer science algorithms. Each topic includes source code in standard programming languages (C++ / Java / Python), time and space complexity breakdowns, and sample test cases.

---

## 📂 Repository Structure

```text
├── 01-Divide-and-Conquer/
│   ├── Binary_Search.cpp
│   ├── Merge_Sort.cpp
│   ├── Quick_Sort.cpp
│   └── Min_Max_Finding.cpp
├── 02-Greedy-Algorithms/
│   ├── Fractional_Knapsack.cpp
│   ├── Job_Sequencing.cpp
│   ├── Prim_MST.cpp
│   ├── Kruskal_MST.cpp
│   └── Dijkstra_Algorithm.cpp
├── 03-Dynamic-Programming/
│   ├── 01_Knapsack.cpp
│   ├── Longest_Common_Subsequence.cpp
│   ├── Matrix_Chain_Multiplication.cpp
│   ├── Bellman_Ford.cpp
│   └── Floyd_Warshall.cpp
├── 04-Backtracking/
│   ├── N_Queens_Problem.cpp
│   ├── Subset_Sum.cpp
│   └── Graph_Coloring.cpp
├── 05-Branch-and-Bound/
│   ├── 01_Knapsack_BNB.cpp
│   └── Travelling_Salesperson.cpp
├── 06-Graph-Algorithms/
│   ├── BFS_DFS_Traversal.cpp
│   ├── Topological_Sort.cpp
│   └── Strongly_Connected_Components.cpp
├── Docs/
│   └── Algorithmic_Complexity_Guide.pdf
└── README.md
```

---

## 🧠 Topics & Algorithms Covered

### 1. Divide and Conquer
* **Binary Search:** O(log n) searching in sorted arrays.
* **Merge Sort:** O(n log n) stable comparison sorting.
* **Quick Sort:** O(n log n) average case divide-and-conquer sorting using pivot partitioning.
* **Strassen's Matrix Multiplication:** Sub-cubic matrix multiplication.

### 2. Greedy Paradigm
* **Fractional Knapsack:** Item selection based on maximum value-to-weight ratio.
* **Job Sequencing with Deadlines:** Maximizing total profit within constraints.
* **Minimum Spanning Trees (MST):** Prim's and Kruskal's Algorithms.
* **Single-Source Shortest Path:** Dijkstra's Algorithm.

### 3. Dynamic Programming (DP)
* **0/1 Knapsack Problem:** Optimal subset selection using tabular/memoization techniques.
* **Longest Common Subsequence (LCS):** String alignment and sequence matching.
* **Matrix Chain Multiplication (MCM):** Optimal parenthesization for matrix chains.
* **All-Pairs Shortest Paths:** Floyd-Warshall Algorithm.

### 4. Backtracking & Branch and Bound
* **N-Queens Problem:** Placing non-attacking queens on an N×N chessboard.
* **Graph Coloring:** Vertex coloring with minimum colors ($K$-colorability).
* **Travelling Salesperson Problem (TSP):** Exact solution state-space tree search.

---

## 📊 Complexity Quick Reference

| Algorithm | Paradigm | Time Complexity (Best) | Time Complexity (Worst) | Auxiliary Space |
| :--- | :--- | :--- | :--- | :--- |
| **Binary Search** | Divide & Conquer | $\mathcal{O}(1)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ |
| **Merge Sort** | Divide & Conquer | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ |
| **Quick Sort** | Divide & Conquer | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(\log n)$ |
| **0/1 Knapsack** | Dynamic Programming | $\mathcal{O}(n \cdot W)$ | $\mathcal{O}(n \cdot W)$ | $\mathcal{O}(n \cdot W)$ |
| **Dijkstra** | Greedy | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}(V)$ |
| **Floyd-Warshall** | Dynamic Programming | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^2)$ |

---

## 💻 How to Run the Code

### Prerequisites
* GCC / G++ Compiler for C++ (`g++ --version`)
* Java Development Kit (JDK) for Java programs
* Python 3.x for Python scripts

### Compilation & Execution (C++ Example)
```bash
# Clone the repository
git clone https://github.com/your-username/DAA-Assignments.git

# Navigate into the project folder
cd DAA-Assignments/01-Divide-and-Conquer

# Compile the file
g++ Merge_Sort.cpp -o Merge_Sort

# Run the executable
./Merge_Sort
```

---

## 🤝 Contributing

Contributions, fixes, and optimizations are welcome! If you find any bug or want to add an alternative approach (e.g., solution in another programming language):

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AwesomeAlgorithm`)
3. Commit your Changes (`git commit -m 'Add solution for Traveling Salesperson'`)
4. Push to the Branch (`git push origin feature/AwesomeAlgorithm`)
5. Open a Pull Request
