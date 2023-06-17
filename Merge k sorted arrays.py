def merge_k_sorted_arrays(arrays):
    # Concatenate all arrays into a single list
    merged = []
    for array in arrays:
        merged.extend(array)
    
    # Sort the merged list
    merged.sort()
    
    # Return the sorted merged list
    return merged

# Example usage
arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
merged_array = merge_k_sorted_arrays(arrays)

# Print the output
print("Arrays:", arrays)
print("Merged Sorted Array:", merged_array)
