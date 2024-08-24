class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1

        while top <= bottom:
            midrow = (top+bottom)//2
            if matrix[midrow][-1] < target:
                top = midrow+1
            elif matrix[midrow][0] > target:
                bottom = midrow-1
            else:
                break

            
        row = (top+bottom)//2
        l, r = 0, len(matrix[row])-1

        while l<=r:
             mid = (l+r)//2

             if matrix[row][mid] == target:
                return True
             elif matrix[row][mid] > target:
                r = mid-1
             elif matrix[row][mid] < target:
                l = mid+1

        return False    
