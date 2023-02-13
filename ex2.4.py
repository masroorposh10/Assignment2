def func2(array, start, end):
    p = array[start]
    i = start - 1
    j = end + 1
    while True:
        i = i + 1
        while array[i] < p:
            i = i + 1
        j = j - 1
        while array[j] > p:
            j = j - 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]
import sys
import time
import json
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    while low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        low = pi + 1

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def main():

    print("Opening File")
    with open("dataset_ex2.json","r") as d:
        data = json.load(d)

    time1 =[]
    time2 = []
    number = []
    print("Assigning Loops")
    for i in range(len(data)):
        start_time = time.time()
        func1(data[i], 0, len(data[i]) - 1)
        end_time = time.time()
        time1.append(end_time - start_time)

        start_time = time.time()
        func2(data[i], 0, len(data[i]) - 1)
        end_time = time.time()
        time2.append(end_time - start_time)

        number.append(i)
        print("Working")


    print("Displaying Graphs")
    fig, ax = plt.subplots()
    ax.plot(number, time1, label='func1')
    ax.plot(number, time2, label='func2')
    ax.set_xlabel("Number of times function called")
    ax.set_ylabel("Time taken")
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()