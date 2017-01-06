class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        import itertools  
        a = []
        alpha = dict()
        alpha['1'] = "None"
        alpha['2'] = "abc"
        alpha['3'] = "def"
        alpha['4'] = "ghi"
        alpha['5'] = "jkl"
        alpha['6'] = "mno"
        alpha['7'] = "pqrs"
        alpha['8'] = "tuv"
        alpha['9'] = "wxyz"
        res = []
        dig = list(str(digits))
        if len(dig) == 1:
            return list(alpha[dig[0]])
        for item in dig:
            res.append(alpha[item])
        for item in list(itertools.product(*res)):
            a.append(str(''.join(item)))
        return a    
            