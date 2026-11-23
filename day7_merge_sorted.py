def merge_sorted_lists(list1, list2):
     # Start with an empty result list
     # the merged answer gets built in here
    merged = []
    # i points at the current number in list1
    # j points at the current number in list2
    # Both start at index 0 (the front of each list)
    i = 0
    j = 0
    # Keep going while BOTH lists still have numbers left to compare
    while i < len(list1) and j < len(list2):
        # Compare the two current numbers and take the smaller one
        if list1[i] <= list2[j]:
            # Append it to the result and move i forward by 1
            merged.append(list1[i])
            i += 1
        else:
            # Append it to the result and move j forward by 1
            merged.append(list2[j])
            j += 1   
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    return merged

# Test 1: two normal sorted lists
print(merge_sorted_lists([1, 2, 4], [1, 3, 4]))

# Test 2: one list is empty — the answer should just be the other list's numbers
print(merge_sorted_lists([], [0]))