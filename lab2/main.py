from math import ceil
import os

bm_dir_path = r'C:\Users\NovaIscariot\PycharmProjects\IS-labs\lab2\balanced_merging'
o_dir_path = r'C:\Users\NovaIscariot\PycharmProjects\IS-labs\lab2\oscillated'


def read_file(path):
    with open(path, 'r') as f:
        data = f.readlines()
    data = " ".join(data)
    return list(map(lambda x: int(x), data.split()))


def list_dir(path):
    files = os.listdir(path)
    for file in files:
        data = read_file(f"{path}\\{file}")
        print(f"{file}: {data} --> {len(data)}")


def cut_to_subfiles(arr, dir_path, files_num, max_items=0):
    subfiles = []
    step = max_items if max_items else ceil(len(arr) / files_num)
    for i in range(0, len(arr), step):
        filename = f"{dir_path}\\cut{len(subfiles)}"
        tmp = arr[i:i+step]
        tmp.sort()
        with open(filename, 'w') as f:
            for item in tmp:
                f.write(f"{item} ")
        subfiles.append(filename)
    return subfiles


def merge_subfiles(file_a, file_b, filename):
    arr_a = read_file(file_a)
    arr_b = read_file(file_b)

    arr_c = []
    len_a, len_b = len(arr_a), len(arr_b)
    idx_a, idx_b = 0, 0

    while idx_a < len_a or idx_b < len_b:
        if idx_a == len_a:
            arr_c.extend(arr_b[idx_b:len_b])
            idx_b = len_b
        elif idx_b == len_b:
            arr_c.extend(arr_a[idx_a:len_a])
            idx_a = len_a
        elif arr_a[idx_a] <= arr_b[idx_b]:
            arr_c.append(arr_a[idx_a])
            idx_a += 1
        else:
            arr_c.append(arr_b[idx_b])
            idx_b += 1

    with open(filename, 'w') as f:
        for item in arr_c:
            f.write(f"{item} ")

    # os.remove(file_a)
    # os.remove(file_b)


def balanced_merging_sort(filename, n):
    data = read_file(filename)
    subfiles = cut_to_subfiles(data, bm_dir_path, n)
    idx = 0

    while len(subfiles) > 1:
        file_a, file_b = subfiles.pop(), subfiles.pop()
        new_filename = f"{bm_dir_path}\\merged{idx}"
        idx += 1
        merge_subfiles(file_a, file_b, new_filename)
        subfiles.append(new_filename)


def oscillated_sort(filename, n):
    data = read_file(filename)
    filenames = [f"{o_dir_path}\\{i+1}.txt" for i in range(n)]
    filelens = [0] * n
    cur_len = n-1
    data_idx = 0
    merge_idx = n-1
    while data_idx < len(data):
        file_idx = 0

        while filelens[file_idx] == 0 and file_idx < n-1 and data_idx < len(data):
            next_data_idx = min(data_idx+cur_len, len(data))
            tmp = data[data_idx:next_data_idx]
            data_idx = next_data_idx
            tmp.sort()
            with open(filenames[file_idx], 'w') as f:
                for item in tmp:
                    f.write(f"{item} ")
            file_idx += 1

        file_idx = 0

        while file_idx < n-1


        list_dir(o_dir_path)
        exit()


'''filename = f'{bm_dir_path}\\unsorted.txt'
balanced_merging_sort(filename, 4)
list_dir(bm_dir_path)'''

print()

filename = f'{o_dir_path}\\unsorted.txt'
oscillated_sort(filename, 4)

