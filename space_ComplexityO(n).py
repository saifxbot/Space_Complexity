def double_elements(arr):
    result = []
    for item in arr:
        result.append(item * 2) # adding each doubled item to the result list
                                # The space complexity is O(n) because we are using a new list to store the results.
                                # The size of the result list grows linearly with the size of the input list. 
    return result

data = [1, 2, 3, 4]
print(double_elements(data))
