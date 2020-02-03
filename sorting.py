
from __future__ import print_function
import time
import numpy as np

class Sorting():

    def __init__(self, arr, algorithm):
        self._arr = arr
        self._algorithm = algorithm
        self._time = time.process_time()
        self.select_sorting()

    def select_sorting(self):        
        if self._algorithm == 'bubble':
            self.bubble_sort()
        elif self._algorithm == 'selection':
            self.selection_sort()
        elif self._algorithm == 'insert':
            self.insertion_sort()
        elif self._algorithm == 'merge':
            self.merge_sort(self._arr)
        elif self._algorithm == 'heap':
            self.heap_sort()
        self._time = time.process_time() - self._time 


    def __repr__(self):
        result = dict([('algorithm', self._algorithm), ('sorted_result', self._arr), ('processed_time', '{:.8f}'.format(self._time))])
        return result # metodo para criar um custom json com __iter__ e retornar o objeto finalizado aqui. 

    def __str__(self):
        return '{:<15}{:10d}({}) : {}'.format(self._algorithm, len(self._arr), self._time)

    def bubble_sort(self):
        n = len(self._arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if self._arr[j] > self._arr[j+1]:
                    self._arr[j], self._arr[j+1] = self._arr[j+1], self._arr[j]
                    swapped = True

            if swapped == False:
                break

    def selection_sort(self):
        n = len(self._arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if self._arr[min_index] > self._arr[j]:
                    min_index = j
            # Swap the minimum index with the first element
            self._arr[i], self._arr[min_index] = self._arr[min_index], self._arr[i]

    def insertion_sort(self):
        n = len(self._arr)
        for i in range(1, n):
            key = self._arr[i]
            j = i-1
            while j >= 0 and key < self._arr[j]:
                self._arr[j + 1] = self._arr[j]
                j -= 1
            self._arr[j + 1] = key

    def merge_sort(self, arr):
        n = len(arr)
        if n > 1:
            mid = n//2 # Finding the mid of the array
            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0
            # Copying the data to temporary arrays
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            # Check if any element was left 
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    def heap_sort(self):
        n = len(self._arr)

        for i in range(n, -1, -1):
            self.heapify(self._arr, n, i)

        for i in range(n-1, 0, -1):
            self._arr[i], self._arr[0] = self._arr[0], self._arr[i]
            self.heapify(self._arr, i, 0)

    def heapify(self, arr, n, i):
        '''
        param:
        arr: array 
        n: is the size of the heap
        i: subtree rooted index
        '''
        largest = i
        left = 2 * i + 1 
        right = 2 * i + 2

        # Check if the left child is greater than root
        if left < n and arr[i] < arr[left]:
            largest = left

        # Check if the right child is greater than root
        if right < n and arr[largest] < arr[right]:
            largest = right
        
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

if __name__ == '__main__':
    algoritmo = ['bubble sort', 'selection sort', 'insertion sort', 'merge sort', 'heap sort']
    size_array = [50, 500]#, 5000, 10000]
    for size in size_array:
        array = np.random.randint(1, 1001, size)
        for alg in algoritmo:
            sorting = Sorting(array, alg)
            sorting.select_sorting()
            print(sorting.__repr__())



'''
def counting_sort(arr, value, exp1):
    n = len(arr)

    if exp1 is None:
        exp1 = 1
    

    output = [0] * n
    count = [0] * value

    for i in range(0, n):
        index = (arr[i]/exp1)
        count[ (index)%10] += 1
    
    for i in range(1, value):
        count[i] += count[i-1]
    
    # build output array
    i = n -1
    while i >=0:
        index = (arr[i]/exp1)
        output[count[ (index)%value ] - 1] = arr[i]
        count[ (index)%value ] -= 1
        i -= 1
    
    i =0
    for i in range(0, n):
        arr[i] = output[i]
    return arr

def radix_sort(arr):
    max_number = max(arr)
    exp = 1
    value = 10
    while max_number/exp > 0:
        counting_sort(arr, value, exp)
        exp *= 10

def bucket_sort(x):
    arr = []
    slot_num = 10 # means 10 slots, each slot's size is 0.1

    for i in range(slot_num):
        arr.append([])
    
    # Put array elements in different buckets
    for j in x: 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 

    for i in range(slot_num):
        arr[i] = insertion_sort(arr[i])
    
    # concatenate result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
'''