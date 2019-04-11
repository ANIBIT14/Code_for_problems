class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        l = []
        for i in A:
            if (i == ')'):
                t = l[-1]
                l.pop()
                f = 1
                while (t != '('):
                    if t in "*+-/":
                        f = 0
                    t = l[-1]
                    l.pop()
                if (f==1):
                    return 1
            else:
                l.append(i)
        return (0)
