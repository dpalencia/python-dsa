# Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up to target.

class TwoSumSolution(object):
    def twoSum(self, nums, target):

        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[target - n] = i


        for i, n in enumerate(nums):
            if n in hashmap:
                if hashmap[n] != i:
                    return [i, hashmap[n]]