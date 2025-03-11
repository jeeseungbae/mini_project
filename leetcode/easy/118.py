from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for row in range(1,numRows+1):
            answer.append([1 for j in range(1,row+1)])

        for i in range(2, numRows):
            for j in range(1, len(answer[i])-1):
                answer[i][j] = answer[i-1][j-1] + answer[i-1][j]

        return answer