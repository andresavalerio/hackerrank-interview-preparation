def plus_minus(arr):
    divisor = len(arr)
    zeros = 0
    positives = 0
    negatives = 0
    for number in arr:
        if number == 0:
            zeros+=1
        elif number > 0:
            positives+=1
        else:
            negatives+=1

    print(f"{positives/divisor:.6f}")
    print(f"{negatives/divisor:.6f}")
    print(f"{zeros/divisor:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)
