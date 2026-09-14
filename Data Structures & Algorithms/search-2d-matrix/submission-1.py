class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def check_row(row):
            if row[-1]>target:
                return True
            else:
                return False
        for i in range(len(matrix)):
            if check_row(matrix[i]):
                if target in matrix[i]:
                    return True
            else:
                if matrix[i][-1]==target:
                    return True 
        return False