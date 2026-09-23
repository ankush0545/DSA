class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        max_water=0
        while left<right:
            width=right-left
            water=min(height[left],height[right])
            current_water=width*water
            max_water=max(max_water,current_water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_water