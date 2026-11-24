import time
import tracemalloc

def measure_algorithm(sort_func, data: list, runs: int = 5) -> tuple:
    total_time_ms = 0.0
    total_peak_kb = 0.0

    for _ in range(runs):
        data_copy = data.copy()

        tracemalloc.start()
        start_time = time.perf_counter()

        sort_func(data_copy)

        end_time = time.perf_counter()
        _, peak_bytes = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        total_time_ms += (end_time - start_time) * 1000
        total_peak_kb += peak_bytes / 1024

    return round(total_time_ms / runs, 4), round(total_peak_kb / runs, 2)
