""" Find the missing number
You are given an array arr containing n-1 distinct integers.
 The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence.
   Your task is to find the missing integer.
"""
def missing_value(list1):
    list_missing = []
    n = list1[-1]  
    full_set = set(range(1, n+1))  
    list1_set = set(list1)  
    list_missing = list(full_set - list1_set) 
    return sorted(list_missing)
arr = input("arr: ")
try:
    list1 = [int(i) for i in arr.split(",")]
except ValueError:
    print("Invalid input. Please enter a list of integers separated by commas.")
else:
    print("arr:", list1)
    if len(list1) > 0:
        mis_value = missing_value(list1)
        if len(mis_value)==1:
            value = mis_value[0]
            print("Output:", value)
        else:
            print("output:",mis_value)
    else:
        print("The list is empty!")