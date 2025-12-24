import threading
import time


# Số vòng lặp tính toán bên trong mỗi "step"
INNER_LOOPS = 100000  # nếu máy yếu, giảm xuống; máy khỏe có thể tăng lên


def cpu_bound_task(thread_name: str, start_step: int = 5, end_step: int = 10):
    """
    Hàm giả lập tác vụ CPU-bound.
    Mỗi step thực hiện 1 vòng for lớn để tiêu CPU, sau đó in ra step.
    """
    for step in range(start_step, end_step):
        total = 0
        for i in range(INNER_LOOPS):
            total += i * i  # phép toán nhỏ nhưng chạy rất nhiều lần

        print(f"{thread_name} -> step {step}")


def run_with_threads(num_threads: int = 4):
    threads = []

    start = time.perf_counter()

    for idx in range(1, num_threads + 1):
        t = threading.Thread(
            target=cpu_bound_task,
            args=(f"Thread-{idx}",),
        )
        threads.append(t)
        t.start()

    # Chờ tất cả thread xong
    for t in threads:
        t.join()

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds")


if __name__ == "__main__":
    run_with_threads()
    print("Done.")
