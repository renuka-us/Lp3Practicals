import timeit
def partition(array, low, high):

  
  pivot = array[high]

  
  i = low - 1

  
  for j in range(low, high):
    if array[j] <= pivot:
      
      i = i + 1

     
      (array[i], array[j]) = (array[j], array[i])

  
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1


def quickSort(array, low, high):
  if low < high:

    
    pi = partition(array, low, high)

    
    quickSort(array, low, pi - 1)

    
    quickSort(array, pi + 1, high)




# non_recursive_time = timeit.timeit("fibonacci(N)", setup=global(), number=RUNS)
# print(f"Fibonacci non-recursive for N = {N} \tTime: {non_recursive_time:.5f} seconds O(n)\tSpace: O(1)")

import random


def quicksort(arr, start , stop):
	if(start < stop):
		
		
		pivotindex = partitionrandome(arr,start, stop)
		
		
		quicksort(arr , start , pivotindex-1)
		quicksort(arr, pivotindex + 1, stop)

def partitionrandome(arr , start, stop):

	
	randpivot = random.randrange(start, stop)

	arr[stop], arr[randpivot] = arr[randpivot], arr[stop]
	return partition(arr, start, stop)

# def partition(arr,low,high):
# 	pivot = arr[high] # pivot
	
# 	# # a variable to memorize where the
# 	# i = start + 1
	
# 	# # partition in the array starts from.
# 	# for j in range(start + 1, stop + 1):
		
# 	# 	# if the current element is smaller
# 	# 	# or equal to pivot, shift it to the
# 	# 	# left side of the partition.
# 	# 	if arr[j] <= arr[pivot]:
# 	# 		arr[i] , arr[j] = arr[j] , arr[i]
# 	# 		i = i + 1
# 	# arr[pivot] , arr[i - 1] =arr[i - 1] , arr[pivot]
# 	# pivot = i - 1
# 	# return (pivot)
# 	i = low - 1

#   # traverse through all elements
#   # compare each element with pivot
# 	for j in range(low, high):
# 		if array[j] <= pivot:
# 		# if element smaller than pivot is found
# 		# swap it with the greater element pointed by i
# 			i = i + 1

# 			# swapping element at i with element at j
# 			(array[i], array[j]) = (array[j], array[i])

# 	# swap the pivot element with the greater element specified by i
# 	(array[i + 1], array[high]) = (array[high], array[i + 1])

# 	# return the position from where partition is done
# 	return i + 1

# Driver Code
if __name__ == "__main__":
     
	array = [8, 7, 2, 1, 0, 9, 6]
	print("Unsorted Array")
	print(array)
	size = len(array)
	print("The lenght of the data is:",size)
	quickSort(array, 0, len(array)-1)
	print('Sorted Array in Ascending Order:')
	print(array)
	non_recursive_time = timeit.timeit("quickSort(array, 0, len(array)-1)", setup=f"from __main__ import quickSort;array={array}", number=100)
	print(f"Fibonacci non-recursive for N = {array} \tTime: {non_recursive_time:.5f} seconds O(n)\tSpace: O(1)")

	
	print("Unsorted array: ")
	print(array)
	print("The lenght is : ",len(array)) ##len is 6
	quicksort(array, 0, len(array) - 1)
	print("The sorted array is: ")
	print(array)
	non_recursive_time = timeit.timeit("quicksort(array, 0, len(array) - 1)", setup=f"from __main__ import quicksort;array={array}", number=100)
	print(f"Fibonacci non-recursive for N = {array} \tTime: {non_recursive_time:.5f} seconds O(n)\tSpace: O(1)")
