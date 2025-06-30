l2 = [1, 2, 5, 4, 3, 9]
print(l2[1:10]) # start from index 1 and go till index 9
print(l2[::2]) # Consider entire list and override the increment to 2
print(l2[::1]) # Defining the default behavior differently
print(l2[::-1]) # Consider entire list but decrement by 1 (increment by -1)
print(l2[1:-1:-1]) # Consider the temp list [2, 5, 4, 3] (in that order) and now move in reverse in this temp list