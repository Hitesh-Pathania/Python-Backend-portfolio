def max_subarray(nums):
    # Start both trackers at the first number, nums[0].
    best_ending_here = nums[0]           # best_ending_here = best run total ending at the current position
    best_so_far = nums[0]                 # best_so_far = biggest run total seen anywhere so far
    for num in nums[1:]:                    # Loop over the remaining numbers, starting from the second one.
        best_ending_here = max(num, best_ending_here + num)                 # the bigger of (num on its own) vs (old best_ending_here + num)

        best_so_far = max(best_so_far, best_ending_here)                    # the bigger of (old best_so_far) vs (new best_ending_here)
    return best_so_far                                                      # After the loop, return best_so_far.


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([1]))
print(max_subarray([-1, -2]))