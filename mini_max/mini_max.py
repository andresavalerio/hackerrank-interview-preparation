def mini_max_sum(arr):
    arr.sort()

    print(f"{sum(arr[:4])} {sum(arr[-4:])}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    mini_max_sum(arr)
