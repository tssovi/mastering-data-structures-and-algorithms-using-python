# Constant Time - O(1)
def get_first(data):
    return data[0]

# Logarithmic Time - O(log n)
def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binary_search(alist[:midpoint],item)
            else:
                return binary_search(alist[midpoint+1:],item)


# Linear Time - O(n)
def linear_search(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1


# Quasi Linear Time - O(n log n)
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr, n):
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


# Quadratic Time - O(n²)
def bubble_sort(arr, n):
   for i in range(n):
      for j in range(0, n-i-1):
         if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
   return arr


# Exponential Time - O(2^n)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# Factorial - O(n!)
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


res_data = []
def heap_permutation(data, n):
    if n == 1:
        res_data.append(data)
        return

    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n - 1] = data[n - 1], data[i]
        else:
            data[0], data[n - 1] = data[n - 1], data[0]
    return res_data


num_arr = [58, 24, 84, 2, 30, 27, 35, 91, 14, 23, 53, 33, 99, 17, 86]
l = len(num_arr)

data = [1, 2, 3]
n = len(data)

sorted_arr = heap_sort(num_arr, l)

val = get_first(num_arr)
print("Result of get_first func is:", val)

val = binary_search(sorted_arr, 17)
print("Result of binary_search func is:", val)

val = linear_search(num_arr, 17)
print("Result of linear_search func is:", val)

val = heap_sort(num_arr, l)
print("Result of heap_sort func is:", val)

val = bubble_sort(num_arr, l)
print("Result of bubble_sort func is:", val)

val = fibonacci(10)
print("Result of fibonacci func is:", val)

val = factorial(10)
print("Result of factorial func is:", val)

val = heap_permutation(data, n)
print("Result of heap_permutation func is:", val)

