def isNumeric(t):
        if t>='0' and t<='9':
            return True
        return False
class Solution(object):
    def myAtoi(self, string):
        if len(string) == 0:
            return 0
        res = 0
        sign = 1
        x = 0
        i = 0
        for k in range(i,len(string)):
            while string[i]==' ' or string[i]=='\t' or string[i]=='\n':
                i+=1
        if string[i] == '-':
            sign = -1 
            i+=1   
        elif string[i] == '+':
            i+=1   
        for j in range(i,len(string)):    
            if string[i] >='0' and string[i]<='9':
                res = res*10 + (ord(string[i]) - ord('0'))
                i+=1
        x = sign*res
        if x > 2147483647:
            return 2147483647
        elif x < -2147483648:
            return -2147483648
        else:
            return x