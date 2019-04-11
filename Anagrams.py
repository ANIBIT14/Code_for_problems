class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        di = {}
        for i in range(len(A)):
           
            tmp = "".join(sorted(A[i]))
            if di.get(tmp,[]) == []:
                di[tmp] = []
                di[tmp].append(i+1)
            else:
                di[tmp].append(i+1)
        return (list(di.values())[::-1])
