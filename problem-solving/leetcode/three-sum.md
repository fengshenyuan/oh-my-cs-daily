```python
from math import ceil
from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Runtime: 344 ms, faster than 99.69% of Python3 online submissions for 3Sum.
        Memory Usage: 18.1 MB, less than 73.54% of Python3 online submissions for 3Sum.

        1.zip the list to a dict;
        2.sort the unique keys
        3.iter the keys to find the target (x, y, z)
            (1).for tuple(x, y, z), lowest = X, then the max candicate z should meet z1 = ceil[|x| / 2] <= z <= 2|x| = z2;
            (2).search the max z from z1, z2
            (3).notice the duplicated elements
        """
        results = []
        stats = defaultdict(int)
        while nums:
            v = nums.pop()
            stats[v] += 1

        keys = sorted(stats.keys())
        while keys:
            x = keys.pop()
            if x < 0:
                search_upper_bound = 2 * abs(x)
                search_lower_bound = ceil(abs(x) / 2)
                for i in range(1, len(keys) + 1):
                    z = keys[-i]
                    if z > search_upper_bound:
                        continue
                    elif z < search_lower_bound:
                        break
                    else:
                        y = 0 - (x + z)
                        if y in stats:
                            zs = stats[z]
                            ys = stats[y]
                            if (y == z and zs >= 2) or (y == x and ys >= 2) or (x != y and y != z):
                                results.append([x, y, z])
            elif x == 0:
                if stats[0] >= 3:
                    results.append([0, 0, 0])
            else:
                break
            del stats[x]
        # print(results)
        return results



def test():
    assert Solution().threeSum([0,0]) == []
    assert Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert Solution().threeSum([-1,0,1,2,-1,-4,3,5,2,0,0]) == [[-4, -1, 5],[-4, 1, 3],[-4, 2, 2],[-1,-1,2],[-1,0,1],[0,0,0]]


if __name__ == '__main__':
    test()
```
