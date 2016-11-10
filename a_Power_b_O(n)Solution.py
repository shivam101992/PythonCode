import math
class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1;
        elif n%2 == 0:
            return math.pow(x, n/2)*math.pow(x, n/2);
        else:
            return x*math.pow(x, n/2)*math.pow(x, n/2);