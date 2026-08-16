# from leetcode
# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    i = 0  # current check point
    for val in nums:
        if val != nums[i]:
            i += 1
            nums[i] = val

    return i + 1


if __name__ == '__main__':
    return removeDuplicates([1, 2,, 3, 5, 5, 6, 7, 7, 8, 9, 10, 12])