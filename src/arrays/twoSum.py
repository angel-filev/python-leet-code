class TwoSum:
    @staticmethod
    def two_sum(nums, target):
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        """
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return None