from collections import Counter

def topKFrequent(nums, k):
    # Count the frequency of each element
    counter = Counter(nums)
    
    # Sort elements by frequency in descending order
    sorted_elements = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)
    
    # Return the top K frequent elements
    return sorted_elements[:k]

# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2
top_k_frequent_elements = topKFrequent(nums, k)
print("The top",k,"frequent elements are:",top_k_frequent_elements)
