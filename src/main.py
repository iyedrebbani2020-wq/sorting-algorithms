from sorting import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
from utils import generate_array, export_to_csv
from benchmark import measure_algorithm

ALGORITHMS = {
    "1": ("Bubble Sort", bubble_sort),
    "2": ("Selection Sort", selection_sort),
    "3": ("Insertion Sort", insertion_sort),
    "4": ("Merge Sort", merge_sort),
    "5": ("Quick Sort", quick_sort),
}

def get_valid_int(prompt: str, min_val: int = 1) -> int:
    while True:
        try:
            val = int(input(prompt))
            if val >= min_val:
                return val
            print(f"Please enter an integer >= {min_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def run_single(choice: str):
    name, func = ALGORITHMS[choice]
    size = get_valid_int("Enter array size (e.g., 1000, 10000, 100000): ")
    data = generate_array(size, "random")
    
    runs = 1 if size >= 50000 else 5
    print(f"\nRunning {name} ({runs} run(s))...")
    avg_time, avg_mem = measure_algorithm(func, data, runs=runs)
    
    print(f"\n--- Results for {name} (n = {size}) ---")
    print(f"Execution Time : {avg_time} ms")
    print(f"Peak Memory    : {avg_mem} KB ({round(avg_mem / 1024, 4)} MB)\n")

def run_comparison():
    sizes = [1000, 5000, 10000, 50000, 100000]
    csv_rows = []

    for size in sizes:
        print(f"\n{'='*15} Array Size: {size} {'='*15}")
        print(f"{'Algorithm':<18} | {'Time (ms)':<12} | {'Memory (MB)':<12} | {'Rank'}")
        print("-" * 55)

        data = generate_array(size, "random")
        results = []

        for _, (name, func) in ALGORITHMS.items():
            if size >= 50000 and name in ["Bubble Sort", "Selection Sort", "Insertion Sort"]:
                results.append((name, float("inf"), 0.0, "Skipped (>50k)"))
                continue

            runs = 1 if size >= 10000 else 5
            t_ms, m_kb = measure_algorithm(func, data, runs=runs)
            m_mb = round(m_kb / 1024, 4)
            results.append((name, t_ms, m_mb, ""))

        valid_results = sorted([r for r in results if r[1] != float("inf")], key=lambda x: x[1])
        ranks = {r[0]: idx + 1 for idx, r in enumerate(valid_results)}

        for name, t_ms, m_mb, note in results:
            if note:
                print(f"{name:<18} | {'N/A':<12} | {'N/A':<12} | {note}")
                csv_rows.append([name, size, "N/A", "N/A", note])
            else:
                rank = ranks[name]
                print(f"{name:<18} | {t_ms:<12} | {m_mb:<12} | #{rank}")
                csv_rows.append([name, size, t_ms, m_mb, rank])

    export_to_csv("results/comparison_results.csv", csv_rows, ["Algorithm", "Array Size", "Time (ms)", "Memory (MB)", "Rank"])
    print("\nResults saved to 'results/comparison_results.csv'.")

def main():
    while True:
        print("\n=========== SORTING ALGORITHMS ===========")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Compare all algorithms")
        print("0. Exit")
        choice = input("Your choice: ").strip()

        if choice == "0":
            print("Exiting program.")
            break
        elif choice in ALGORITHMS:
            run_single(choice)
        elif choice == "6":
            run_comparison()
        else:
            print("Invalid option. Please choose between 0 and 6.")

if __name__ == "__main__":
    main()
