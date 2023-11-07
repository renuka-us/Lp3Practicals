import random
import time

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = []
    greater = []
    equal = []
    for element in arr:
        if element < pivot:
            lesser.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    return deterministic_quick_sort(lesser) + equal + deterministic_quick_sort(greater)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    lesser = []
    greater = []
    equal = []
    for element in arr:
        if element < pivot:
            lesser.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    return randomized_quick_sort(lesser) + equal + randomized_quick_sort(greater)

def main():
    while True:
        print("Quick Sort Analysis")
        print("1. Perform Deterministic Quick Sort")
        print("2. Perform Randomized Quick Sort")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            arr = input("Enter a list of numbers separated by spaces: ")
            arr = list(map(int, arr.split()))
            start_time = time.time()
            sorted_arr = deterministic_quick_sort(arr)
            end_time = time.time()
            print("Sorted array:", sorted_arr)
            print("Time taken:", end_time - start_time, "seconds")

        elif choice == "2":
            arr = input("Enter a list of numbers separated by spaces: ")
            arr = list(map(int, arr.split()))
            start_time = time.time()
            sorted_arr = randomized_quick_sort(arr)
            end_time = time.time()
            print("Sorted array:", sorted_arr)
            print("Time taken:", end_time - start_time, "seconds")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
