import time
import random
from function_utils import max_search

def study_performance(n, max_value=20, len=10):
    time_list = []

    for i in range(n):
        start_time = time.time()
        x = random.sample(range(1, max_value), len)
        # call our function to search the largest number
        max_val, index_max = max_search(x)
        #print("max:", max_val)

        process_time = time.time() - start_time
        time_list.append(process_time)

    print("Avg execution time of the function: ", sum(time_list)/n, " [s]")

def main():
    study_performance(n=100, max_value=50, len=20)

if __name__ == "__main__":
    main()

