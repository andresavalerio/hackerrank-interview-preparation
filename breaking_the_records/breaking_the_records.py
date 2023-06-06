import os

def breakingRecords(scores):
    min_value = scores[0]
    max_value = scores[0]
    min_counter = 0
    max_counter = 0

    for score in scores:
        if score < min_value:
            min_value = score
            min_counter += 1
        elif score > max_value:
            max_value = score
            max_counter += 1

    return [max_counter, min_counter]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
