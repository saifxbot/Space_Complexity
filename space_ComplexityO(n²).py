def print_all_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j) # This function prints all pairs of elements in the array.
                        # The space complexity is O(n^2) 
                        #because we are generating pairs for each element

data = [1, 2, 3]
print_all_pairs(data)
