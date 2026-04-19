import random
import time
import pandas as pd

with open('data.txt', 'w') as f:
    for i in range(100, 10_001, 100):
        sublist = [str(random.randint(-100_000, 100_000)) for _ in range(i)]
        f.write(' '.join(sublist) + '\n')


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

    return (arr, work_time, total_iterations)


def main():
    list_of_arrays = []
    list_of_work_times = []
    list_of_total_iterations = []
    list_of_len_of_arrays = []
    with open('data.txt', 'r') as f:
        for array in f.readlines():
            list_array = list(map(int, array.split()))
            total_result_of_sort = shell_sort(list_array)
            list_of_arrays.append(total_result_of_sort[0])
            list_of_work_times.append(total_result_of_sort[1])
            list_of_total_iterations.append(total_result_of_sort[2])
            list_of_len_of_arrays.append(len(list_array))
        data = {
            'len_of_arrays': list_of_len_of_arrays,
            'work_times': list_of_work_times,
            'total_iterations': list_of_total_iterations
        }
    df = pd.DataFrame(data)
    df.to_excel('Total.xlsx', index=False)


if __name__ == '__main__':
    main()
