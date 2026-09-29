"""
You are given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order."""

#My Solution
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashMap: dict ={}
    for i, num in enumerate(nums):
        hashMap[i]=num

    for key, val in hashMap.items():
        if target-val in hashMap.values():
            second: int = next((k for k, v in hashMap.items() if v==target-val and k!=key),None)
            if second:
                return [key, second]

"""
This solution ism't complex, but can be made simpler by inversing the index and numbers as keys and values.
My mindset behind this was me accounting for how a list could have duplicate numbers, such as [3,3].
Which is why I was so hesitant to make the actual numbers keys. However, even though there'd be only
one of the two numbers as a key in the hashmap, what we can guarantee is that the number in the hashmap
would be the number with the latest index. This means if we were to loop through the list of numbers,
eventually when we are on the number that comes before its twin, we can simply test to see if any number
within the hashmap adds to the target, and then simply return the value (index) that it is set to in the hashmap."""

# The simple idea put into practice

def twoSum2(self, nums: List[int], target: int) -> List[int]:
    hashMap: dict ={}
    for i, num in enumerate(nums):
        hashMap[num]=i

    for i,num in enumerate(nums):
        diff = target-num
        if diff in nums and hashMap[diff]!=i:
            return [i,hashMap[diff]]

    