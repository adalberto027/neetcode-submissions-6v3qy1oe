class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]

        for e in nums:
            pre.append(pre[-1] * e)
        for e in reversed(nums):
            post.append(post[-1] * e)
        
        pre.append(1)
        post.append(1)

        post.reverse()

        ans = []

        for i in range(len(nums)):
            ans.append(pre[i] * post[i+2])
            
        return ans
        