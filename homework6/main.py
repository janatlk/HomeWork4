def get_list() -> list:
    return list(range(0, 1000000000, 2))
"""
    what is Binary Search?
    then do Solution for search target in list
"""


class Solution:
    """
        find_target -> YOUR_CODE
    """

    def find_target(self, list, target):
        right = len(list)-1
        left = 0
        while left <= right:
            middle = int(left+right)//2
            guess = list[middle]

            if guess == target:
                return middle
            if guess > target:
                right = middle-1
            else:
                left = middle + 1
        return (left,right)
print(Solution().find_target(get_list(),500))