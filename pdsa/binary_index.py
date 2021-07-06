# Binary index tree
# Keep track of cumulative sums
# Represented as a list

class BIT():
    def __init__(self, input_arr):
        self.input_arr = input_arr
        self.bit = [0] * (len(self.input_arr) + 1)
        self.build()

    def build(self):
        """
            Initial tree build
        """
        for i in range(1, len(self.input_arr) + 1):
            self.update(i)

    def update(self, index):
        """
            Update a particular element
        """
        num = self.input_arr[index - 1]
        while index <= len(self.input_arr):
            print(index)
            self.bit[index] = self.bit[index] + num
            print(self.bit)
            index = index + (index & -index)
            
            


    def sum(self, index):
        """
            Cumulative sum at a particular index
        """
        total_sum = 0
        while index >= 1:
            total_sum = total_sum + self.bit[index]
            index = index - (index & -index)
            print(str(index) + ": " + str(self.bit[index]))
        return total_sum
    