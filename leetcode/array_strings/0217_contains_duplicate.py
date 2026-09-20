# My solution:
def containsDuplicate(self, nums: list[int]) -> bool:
    numberDict: dict = {}
    for i in range(len(nums)):
        numberDict[nums[i]]=i
    if (len(numberDict)<len(nums)):
        return True
    else:
        return False

""" 
    THOUGHT PRCOESS:
My first initial thought process was to use the fact that dictionaries cannot contain multiple of the same key,
and so I used this fact to then compare the lengths of the dictionary to the list. If the list has greater length
than the dictionary, that must mean there was a duplicate, returning true. False otherwise.

Time Complexity: O(n), but always takes the worst case scenario of time since it doesn't end early.

    REFLECTION:
Upon reflection, it had been much better to simply use a set. They are essentially dictionaries without key: value pairs
and only the keys. However, sets are a concept I had recently learned, but now thinking about it in a way where sets are
just simply dictionaries with no values, I believe my usage of them will start becoming much more prominent. Also, using a for
loop with range(len()) is unnecessary and it'd be a little better to just use for i in nums.
"""

#Neetcode solution

def containsDuplicateNeet(self, nums: list[int]) -> bool:
    hashSet: set = set()
    for i in nums:
        if (i in hashSet):
            return True
        else:
            hashSet.add(i)
    return False
#Time complexity is also O(n) but can end early if duplicate is found



