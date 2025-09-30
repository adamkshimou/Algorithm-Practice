class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # return order: 1 2 3 6 9 8 7 4 5
        res = []
        while matrix:

            res+=(matrix.pop(0))

            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            if matrix:
                res+=(matrix.pop()[::-1])
            
            if matrix and matrix[0]:

                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res
