'''
Solution: 1-pass hashmap
1. iterate through nums list
2. calculate the num required to get the target from i (complement)
3. if the complement is found in the hashmap, return the indices
4. otherwise, store the num as a key and its index as a val in the hashmap
5. if no complement is found, return an empty list (two-sum doesn't exist)

Time complexity: O(n)
    List of n elements is traveresed at most once.
    Lookup cost is O(1)

Space complexity: O(n)
    Hashmap stores at most n elements

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

        return []