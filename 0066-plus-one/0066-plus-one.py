class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        result = []

        # Iterate over digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            current_sum = digits[i] + carry
            result.append(current_sum % 10)  # Append the new digit to the result
            carry = current_sum // 10  # Update the carry

        # If there is a remaining carry, add it to the result
        if carry:
            result.append(carry)

        # Reverse the result as it was constructed from right to left
        return result[::-1]

# Example usage:
sol = Solution()
digits1 = [1, 2, 3]
print(sol.plusOne(digits1))  # Output: [1, 2, 4]

digits2 = [4, 3, 2, 1]
print(sol.plusOne(digits2))  # Output: [4, 3, 2, 2]

digits3 = [9]
print(sol.plusOne(digits3))  # Output: [1, 0]
