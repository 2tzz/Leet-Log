class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for list_item in matrix :
            new_set = set(list_item)
            if target in new_set :
                return True
            else :
                continue
        return False