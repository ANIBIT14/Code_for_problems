class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A = sorted(A)
        cl = 0
        for i in range(len(A) - 2):
            j, k = i + 1, len(A) - 1
            while k > j:
                su = A[i] + A[j] + A[k]
                if  su == B:
                    return su
                if cl is 0 or abs(B - su) < abs(B - cl):
                    cl = su
                if su < B:
                    j += 1
                else:
                    k -= 1
        return cl