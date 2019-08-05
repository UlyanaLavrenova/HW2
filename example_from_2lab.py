import random
import datetime
import prettytable
import matplotlib.pyplot as plt

def BubbleSort (A):
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a


def QuickSort (A, first, last):
    if first >= last:
        return
    pivot = A[first]
    first_bigger = first + 1
    while first_bigger <= last:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= last:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger -1
    A[first], A[last_smaller] = A[last_smaller], A[first]
    QuickSort(A, first, last_smaller - 1)
    QuickSort(A, first_bigger, last)


table = prettytable.PrettyTable(["Size", "Bubble time", "Quick time"])
x = []
y1 = []
y2 = []


for N in range (1000,5001,1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    B = A.copy()

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()
    y2.append((t4-t3).total_seconds())
    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)
plt.plot(x, y1, "C2")
plt.plot(x, y2, "C1")
plt.show()