import sys
import timeit
import json
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
    
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

with open("dataset.txt","r") as d:
    data = json.load(d)

time1 =[]
time2 = []
number = []
for i in range(len(data)):
    time1.append(timeit.timeit(lambda: func1(data[i],i,len(data[i])-1), number=1))
    time2.append(timeit.timeit(lambda: func2(data[i],i,len(data[i])-1), number=1))
    number.append(i)

plt.plot(number,time1)
plt.xlabel("Number of times function called ")
plt.ylabel("Time taken")
plt.show()

plt.plot(number,time2)
plt.xlabel("Number of times function called ")
plt.ylabel("Time taken")
plt.show()