class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_order = [1]
        post_order = [1]

        for i in range(len(nums)):
            pre_order.append(pre_order[-1] * nums[i])
            post_order.append(post_order[-1] * nums[-(i + 1)])
        
        ans = []
        for i in range(len(nums)):
            ans.append(pre_order[i] * post_order[-(i+2)])
        return ans

        
        