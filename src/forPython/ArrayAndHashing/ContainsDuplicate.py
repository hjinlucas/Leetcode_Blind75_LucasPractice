'''
Easy:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
nums = [1, 2, 3, 1]
'''

'''
Thoughts:
nums = [1, 2, 3, 1]
There are multiple solutions for this quesions:
First, we can use the straight way: iterate each value in the array to see if there is a duplicate of it; Time: O(n^2), Space: O(1)
Then, we can try to sort the array, we get [1, 1, 2, 3], if the array is sorted, the duplicate will be next to each other, we only need to
    check the value in the next index. Time: O(nlogn), Space: O(1); 
However, we still find another to reduce the time complexity, sacrifice some memory: we can use hashset, [ ], put the values of this array in 
    the hashset and iterate, check if there is duplicate in the hashset. Time: O(n), Space: O(n)
    [1, ]  [1, 2, 3, 1]
'''
class ContainsDuplicate(object):
    def containsDuplicate(self, nums):
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        
cd = ContainsDuplicate()
print(cd.containsDuplicate([1, 2, 3, 1])) # True



