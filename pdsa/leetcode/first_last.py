"""Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity."""


class FirstLastIndices(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        self.low_index = -1
        self.high_index = -1
        self.left_binary_search(0, len(nums) - 1)
        self.right_binary_search(0, len(nums) - 1)
        return [self.low_index, self.high_index]
    
    def left_binary_search(self, i, j):
        mid_right = i + int((j - i + 1) / 2)
        mid_left = mid_right - 1
        if self.nums[mid_right] == self.target:
            if self.nums[mid_left] < self.target:
                self.low_index = mid_right
                return

        if j == mid_right:
            return

        if self.nums[mid_right] < self.target:
            self.left_binary_search(mid_right + 1, j)
        else:
            self.left_binary_search(i, mid_left)
    
    def right_binary_search(self, i, j):
        mid_right = i + int((j - i + 1)  / 2)
        mid_left = mid_right - 1
        if self.nums[mid_left] == self.target:
            if self.nums[mid_right] > self.target:
                self.high_index = mid_left
                return

        if j == mid_right:
            return

        if self.nums[mid_left] > self.target:
            self.right_binary_search(i, mid_left)
        else:
            self.right_binary_search(mid_right + 1, j)

    

if __name__ == "__main__":
    soln = FirstLastIndices()
    soln.searchRange([5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,10], 8)
    print(soln.low_index)
    print(soln.high_index)