def find_k_maximum_sum_combinations(A, B, K):
    # Create a list to store the sum combinations
    combinations = []
    
    # Iterate through all possible combinations of elements from arrays A and B
    for a in A:
        for b in B:
            # Calculate the sum and add it to the combinations list
            combinations.append((a + b, (a, b)))
    
    # Sort the combinations in descending order based on the sum
    combinations.sort(reverse=True)
    
    # Retrieve the maximum K sum combinations
    return combinations[:K]

# Example usage
A = [3, 2]
B = [1, 4]
K = 2
combinations = find_k_maximum_sum_combinations(A, B, K)

# Print the output
print("Array A:", A)
print("Array B:", B)
print("K:", K)
print("Maximum K Sum Combinations:")
for combination in combinations:
    sum_comb, (a, b) = combination
    print(sum_comb, "// (A:", a, ") + (B:", b, ")")
