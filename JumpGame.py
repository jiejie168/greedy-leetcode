__author__ = 'Jie'
"""

"""

class Solution:
    def canJump(self, nums) -> bool:
        n=len(nums)
        i=0
        reach=0
        while i<n and i<=reach:
            reach=max(reach,i+nums[i])
            if reach>=n-1:
                return True
            i+=1
        return False

solution=Solution()
nums=[3,2,1,0,4]
ans=solution.canJump(nums)
print(ans)