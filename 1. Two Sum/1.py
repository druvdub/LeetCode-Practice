from typing import List


class Solution:

    '''
    One-pass Hash Table

    Time complexity : O(n)
    Space complexity : O(n)

    '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        for i in range(0, len(nums)):
            res = target - nums[i]
            if res in hmap:
                return [i, hmap[res]]
            hmap[nums[i]] = i
        return []

    '''
    Brute Force

    Time complexity : O(n^2)
    Space complexity : O(1)
    
    '''

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    '''
    Two-pass Hash Table

    Time complexity : O(n)
    Space complexity : O(n)

    '''

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        for i in range(0, len(nums)):
            hmap[nums[i]] = i
        for i in range(0, len(nums)):
            res = target - nums[i]
            if res in hmap and hmap[res] != i:
                return [i, hmap[res]]
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    # nums = [3, 2, 4]
    # target = 6
    # nums = [3, 3]
    # target = 6
    s = Solution()
    print(s.twoSum(nums, target))
    print(s.twoSum2(nums, target))
    print(s.twoSum3(nums, target))
