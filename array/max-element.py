def find_max_element(arr):
    max_element = arr[0]

    for num in arr:
        if num > max_element:
            max_element = num
        
    return max_element

    


arr = [1,2,3,6,5]
maximum_element = find_max_element(arr)
print("Maximum Element: ",maximum_element)