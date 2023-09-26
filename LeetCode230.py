class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_array = []
        postfix_array = [0] * (len(nums))

        prefix = 1
        postfix = 1

        j = len(nums)-1
        i = 0
        product_array = []

        while i< len(nums):
            prefix_array.append(prefix)
            prefix *= nums[i]
            print("j is", j)
            postfix_array[j] = postfix
            postfix *=nums[j]

            i +=1
            j -=1

        for i in range(0,len(nums)):
            product_array.append(prefix_array[i] * postfix_array[i])
        return product_array   
       
            
