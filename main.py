from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  seen = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
      return [seen[complement], i]
    seen[num] = i
  return


# testcases = [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]

# for i, (nums, target) in enumerate(testcases, 1):
#   result = twoSum(nums, target)
#   print(f"Example {i}: {result}")