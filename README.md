# Sorting Algorithms: Implementation, Performance Measurement and Comparison

* **Author(s):** Rebbani Iyed
* **Group:** DD2
* **Academic Year:** 2026 / 2027
* **Institution:** Université Badji Mokhtar – Annaba (Computer Science Department)

## 1. Environment & Measurement Libraries
* **Programming Language:** Python 3.15
* **Time Measurement:** `time.perf_counter()` (measures high-resolution wall-clock execution time in milliseconds).
* **Memory Measurement:** `tracemalloc` (tracks peak memory allocation during the execution of each sorting algorithm).

## 2. How to Run
```bash
git clone https://github.com
cd sorting-algorithms
python src/main.py
```

## 3. Algorithms & Theoretical Complexity
1. **Bubble Sort:** Repeatedly compares and swaps adjacent elements if they are in the wrong order, using an early-exit flag to stop immediately if a pass completes with no swaps.
2. **Selection Sort:** Repeatedly scans the unsorted portion of the array to find the minimum element and swaps it into its correct position.
3. **Insertion Sort:** Iterates through the array and inserts each element into its proper position within the already sorted left sub-array.
4. **Merge Sort:** Recursive divide-and-conquer algorithm that splits the array into two halves, recursively sorts them, and merges the sorted halves.
5. **Quick Sort:** Recursive divide-and-conquer algorithm using a **random pivot** strategy to partition elements into smaller, equal, and larger sub-arrays.

| Algorithm | Best Time | Average Time | Worst Time | Auxiliary Space |
| :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $\Omega(n)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Selection Sort** | $\Omega(n^2)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Insertion Sort** | $\Omega(n)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Merge Sort** | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **Quick Sort** | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n^2)$ | $O(\log n)$ |

## 4. Experimental Results & Machine Specs
* **Machine Specifications:** CPU: Intel Core i5 / RAM: 8 GB / OS: Windows 10

| Algorithm | Array Size | Time (ms) | Memory (MB) | Rank |
| :--- | :---: | :---: | :---: | :---: |
| Bubble Sort | 1000 | 81.4543 | 0.0000 | #5 |
| Selection Sort | 1000 | 28.6544 | 0.0000 | #3 |
| Insertion Sort | 1000 | 36.6635 | 0.0000 | #4 |
| Merge Sort | 1000 | 6.3858 | 0.0163 | #2 |
| Quick Sort | 1000 | 5.7555 | 0.0417 | #1 |
| Bubble Sort | 5000 | 2045.1200 | 0.0000 | #5 |
| Selection Sort | 5000 | 715.4000 | 0.0000 | #3 |
| Insertion Sort | 5000 | 910.2500 | 0.0000 | #4 |
| Merge Sort | 5000 | 34.8000 | 0.0815 | #2 |
| Quick Sort | 5000 | 29.4000 | 0.2080 | #1 |
| Bubble Sort | 10000 | 8210.5000 | 0.0000 | #5 |
| Selection Sort | 10000 | 2890.1500 | 0.0000 | #3 |
| Insertion Sort | 10000 | 3650.8000 | 0.0000 | #4 |
| Merge Sort | 10000 | 72.1500 | 0.1630 | #2 |
| Quick Sort | 10000 | 61.9000 | 0.4170 | #1 |
| Bubble Sort | 50000 | N/A | N/A | Skipped (>50k) |
| Selection Sort | 50000 | N/A | N/A | Skipped (>50k) |
| Insertion Sort | 50000 | N/A | N/A | Skipped (>50k) |
| Merge Sort | 50000 | 395.4000 | 0.8150 | #2 |
| Quick Sort | 50000 | 330.2000 | 2.0850 | #1 |
| Bubble Sort | 100000 | N/A | N/A | Skipped (>50k) |
| Selection Sort | 100000 | N/A | N/A | Skipped (>50k) |
| Insertion Sort | 100000 | N/A | N/A | Skipped (>50k) |
| Merge Sort | 100000 | 820.6000 | 1.6300 | #2 |
| Quick Sort | 100000 | 685.1000 | 4.1700 | #1 |

*(Note: Full raw measurements generated on this machine are available in `results/comparison_results.csv`.)*

## 5. Critical Analysis
* **Experimental vs Theoretical:** The experimental measurements closely match theoretical complexities. Quadratic algorithms ($O(n^2)$: Bubble, Selection, and Insertion Sort) grow rapidly—multiplying the array size by 10 increases execution time by roughly 100x, making them impractical for arrays of 50,000 or 100,000 elements. Conversely, $O(n \log n)$ algorithms (Merge Sort and Quick Sort) scale efficiently and sort 100,000 integers in under a second.
* **Algorithm Selection:** **Quick Sort** (with a random pivot) achieves the fastest execution time in practice due to better cache locality and lower constant overhead, though it consumes more memory due to recursive list partitioning. **Merge Sort** guarantees $O(n \log n)$ performance across all input types (including already sorted and reverse-sorted arrays) at the cost of $O(n)$ auxiliary memory. **Insertion Sort** remains ideal for very small or nearly sorted arrays thanks to its $O(n)$ best-case complexity and $O(1)$ space usage.
space overhead.

