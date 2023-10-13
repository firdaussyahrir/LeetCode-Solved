from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store elements and their indices
        num_indices = {}
        
        for index, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # If the complement exists in the dictionary, return its index along with the current index
            if complement in num_indices:
                return [num_indices[complement], index]
            
            # Otherwise, store the current number and its index in the dictionary
            num_indices[num] = index
        
        # If no solution is found, return an empty list (this should not happen based on the problem constraints)
        return []
