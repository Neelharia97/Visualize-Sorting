import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation    

# def display(A, size):
#     for i in range(size):
#         print(A[i]," ")

# def mergeSort():

# def quickSort(A, start, end):
#     if start>=end:
#         return
    
#     pivot = A[end]
#     for i in range(start, end):
#         if A[i]<pivot:
def animate(A,size):
    for i in range(size-1):
        plt.scatter(i,A[i])


def bubbleSort(A, size):
    for i in range(size-1):
        flag = 0
        for j in range(size-i-1):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                flag = 1 
        if flag == 0:
            break
    animate(A,size)

# if __name__ == "__main__":





a = [1,2,4,3,0]
size = len(a)
print(bubbleSort(a,size))
animate(a,size)

