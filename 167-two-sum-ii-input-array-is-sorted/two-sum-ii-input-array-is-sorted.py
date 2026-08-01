class Solution(object):
    def twoSum(self, numbers, target):
        i0 = 0
        i1 = len(numbers) - 1

        while i0 < i1:
            sum = numbers[i0] + numbers[i1]
            if sum == target:
                return [i0+1, i1+1]
            elif sum > target:
                i1 -= 1
            else:
                i0 += 1
        return []
