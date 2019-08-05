import random
import datetime
import prettytable
import matplotlib.pyplot as plt


def InsertSort (A):
    B = A.copy()
    for i in range(len(B)):
        t = B[i]
        j = i
        while j != 0:
            if B[j-1] > t:
                B[j] = B[j-1]
                j -= 1
            else:
                break
        B[j] = t
    #print(B)


def MergeSort (A):
    if len(A) <= 1:
        return A
    middle = int(len(A)/2)
    left = MergeSort(A[:middle])
    right = MergeSort(A[middle:])
    return Merge(left, right)


def Merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(right) > 0:
        result += right
    if len(left) > 0:
        result += left
    return result


def QuickSort(A, sm, em):
    if sm >= em:
        return
    i, j = sm, em
    pivot = A[random.randint(sm, em)]

    while i <= j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i, j = i + 1, j - 1
    QuickSort(A, sm, j)
    QuickSort(A, i, em)


table = prettytable.PrettyTable(["Size of list", "InsertSort time", "MergeSort time", "QuickSort time"])
x = []
y1 = []
y2 = []
y3 = []


for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    t1 = datetime.datetime.now()
    InsertSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())

    t3 = datetime.datetime.now()
    MergeSort(A)
    t4 = datetime.datetime.now()
    y2.append((t4-t3).total_seconds())

    t5 = datetime.datetime.now()
    QuickSort(A, 0, len(A)-1)
    t6 = datetime.datetime.now()
    y3.append((t6-t5).total_seconds())

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds()), str((t6-t5).total_seconds())])
print(table)
plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C5")
plt.show()



#-----------------------

"""print(A)
InsertSort(A)
B = MergeSort(A)
print(B)
QuickSort(A, 0, len(A)-1)
print(A)"""

