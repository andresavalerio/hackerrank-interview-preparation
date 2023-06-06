import os
from datetime import time, datetime

def time_conversion(s):
    ampm_hours = datetime.strptime(s, "%I:%M:%S%p")

    datetime_time = ampm_hours.time()

    military_hours = datetime_time.strftime("%H:%M:%S")

    return military_hours

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = time_conversion(s)

    fptr.write(result + '\n')

    fptr.close()
