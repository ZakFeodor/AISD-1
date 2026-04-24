import pandas as pd
from shell_sort import shell_sort
from generate_file import generate_file


def main():
    generate_file('data')

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
