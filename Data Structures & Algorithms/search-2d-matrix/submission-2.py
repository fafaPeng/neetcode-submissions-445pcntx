class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     rows = len(matrix)
    #     cols = len(matrix[0])
    #     r = 0
    #     c = cols-1
    #     while r<rows and c<cols and c>=0:
    #         if matrix[r][c] == target:
    #             return True
    #         elif matrix[r][c] < target:
    #             r+=1
    #         elif matrix[r][c] > target:
    #             c-=1
    #     return False
     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows - 1
        while top <= bottom: 
            row = (top+bottom)//2
            if target < matrix[row][0]:
                bottom = row -1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        left = 0
        right = cols -1
        while left <= right:
            middle = (left+right)//2
            if matrix[row][middle] < target:
                left = middle + 1
            elif matrix[row][middle]>target:
                right = middle - 1
            else:
                return True
        return False

            
