class Solution:
    def checkDublicates(self, answer: List[List[int]]) -> List[List[int]]:
        cp = answer
        for i in range(len(answer)):
            for j in range(i + 1, len(answer)):
                if self.oneToThree(answer[i][0], answer[j]) and self.oneToThree(answer[i][1], answer[j]) and self.oneToThree(answer[i][2], answer[j]):
                    cp[j] = []
        return [sublist for sublist in cp if sublist]

    def oneToThree(self,  a: int, ls: List[int]) -> bool:
        return a in ls[:3]

    def addToZero(self, curr: List[int]) -> bool:
        return (curr[0] + curr[1] + curr[2]) == 0

    def notSame(self, curr: List[int]) -> bool:
        return (curr[0] != curr[1]) and (curr[0] != curr[2]) and (curr[1] != curr[2])

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # three numbers which don't equal each other
        # add up to zero
        answer = []
        c1 = nums
        c2 = nums
        c3 = nums

        for i in range(len(c1)):
            for j in range(i + 1, len(c1)):
                for k in range(j + 1, len(c1)):
                    curr = [c1[i], c2[j], c3[k]]
                    if self.addToZero(curr) and self.notSame(curr):
                        answer.append(curr)

        answer = self.checkDublicates(answer)

        return answer

   