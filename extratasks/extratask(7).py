m=0
d = 0
d2 = 0
class Solution:
    def maximum_wealth(self, account: list) -> int:
        for i in account:
            if m < 1:
                d += sum(i)
                m += 1
            if m < 2:
                d2 += sum(i)
                m += 1


            if d > d2:
                print(d)
            elif d < d2:
                print(d2)
            else:
                pass



M = Solution().maximum_wealth([[1,2,3],[4,5,6],[1,2]])

