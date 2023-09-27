class Solution:
    def maxArea(self, height: List[int]) -> int:

        l , r = 0, 1

        max_area= 0

        while l<r and r < len(height):
           
            area = (r-l) * min(height[l], height[r])
           
            max_area = max(max_area, area)
 
            if height[l] < height[r]:
                l =r
                r+=1
            else:
                r+=1

        return max_area
        
