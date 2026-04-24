import time


def shell_sort(arr):
    time_start = time.time()
    n = len(arr)
    gap = n // 2
    total_iterations = 0

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                total_iterations += 1

            arr[j] = temp

        gap //= 2

    time_end = time.time()
    work_time = time_end - time_start

    return arr, work_time, total_iterations
