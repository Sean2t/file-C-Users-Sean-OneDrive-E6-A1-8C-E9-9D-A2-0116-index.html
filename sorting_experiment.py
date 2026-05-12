import time
import random

# 1. Counting Sort 實作
def counting_sort(arr, k=65536):
    n = len(arr)
    B = [0] * n
    C = [0] * k
    # Loop 2: 統計頻率
    for x in arr:
        C[x] += 1
    # Loop 3: 累加位置
    for i in range(1, k):
        C[i] += C[i-1]
    # Loop 4: 放置元素 (由後往前以維持穩定性)
    for i in range(n - 1, -1, -1):
        B[C[arr[i]] - 1] = arr[i]
        C[arr[i]] -= 1
    return B

# 2. Radix Sort 實作 (使用 Base 256, 16-bit 需跑兩輪)
def radix_sort(arr):
    # 第一輪：針對低 8 位 (LSD)
    def get_digit(num, d):
        return (num >> (d * 8)) & 0xFF

    def counting_sort_for_radix(a, d):
        n = len(a)
        B = [0] * n
        C = [0] * 256
        for x in a:
            C[get_digit(x, d)] += 1
        for i in range(1, 256):
            C[i] += C[i-1]
        for i in range(n - 1, -1, -1):
            digit = get_digit(a[i], d)
            B[C[digit] - 1] = a[i]
            C[digit] -= 1
        return B

    arr = counting_sort_for_radix(arr, 0) # LSD
    arr = counting_sort_for_radix(arr, 1) # MSD (16-bit)
    return arr

# 實驗設定
def run_experiment():
    N = 1000000  # 1M 筆資料
    # 產生 16-bit unsigned integer (0 ~ 65535)
    data = [random.randint(0, 65535) for _ in range(N)]
    
    print(f"開始實驗，樣本數: {N}, 鍵值範圍: 0-65535\n")

    # A. Python 內建 sorted() (Timsort)
    start = time.time()
    res_builtin = sorted(data)
    print(f"Python sorted()   時間: {time.time() - start:.4f} 秒")

    # B. Counting Sort
    start = time.time()
    res_counting = counting_sort(data)
    print(f"Counting Sort     時間: {time.time() - start:.4f} 秒")

    # C. Radix Sort
    start = time.time()
    res_radix = radix_sort(data)
    print(f"Radix Sort (LSD)  時間: {time.time() - start:.4f} 秒")

if __name__ == "__main__":
    run_experiment()