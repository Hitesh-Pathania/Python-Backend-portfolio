def two_sum(nums, target):
seen = {}
for i, x in enumerate(nums):
need = target - x
if need in seen:
return [seen[need], i]
seen[x] = i
print(two_sum([2, 7, 11, 15], 9)) # expect [0, 1]
print(two_sum([3, 2, 4], 6)) # expect [1, 2]
print(two_sum([3, 3], 6))