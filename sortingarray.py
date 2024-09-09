'''
Sort an Array of 0s, 1s, and 2sYou are given an array arr consisting only of 0s, 1s, and 2s. 
The task is to sort the array in increasing order in linear time (i.e., O(n)) without using any extra space.
 This means you need to rearrange the array in-place.
'''

def sort_in_ascending_order(arr):
    sorted_arr = []
    while(len(arr) != 0):
        smallest = arr[0]
        index = 0
        for i in range(1, len(arr)):
            if smallest > arr[i]:
                index = i
                smallest = arr[i]
        sorted_arr.append(smallest)
        smallest = arr[0]
        del arr[index]
    return sorted_arr

array_input = input("Enter the array: ")
try:
    arr = [int(i) for i in array_input.split(",")]
except ValueError:
    print("Invalid input. Please enter a list of integers separated by commas.")
else:
    print("Input array:", arr)
    if len(arr) > 0:
        sorted_array = sort_in_ascending_order(arr)
        print("Sorted Output:", sorted_array)
    else:
        print("The list is empty!")

       