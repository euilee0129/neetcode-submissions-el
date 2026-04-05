class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alpha1, alpha2 = {}, {}
        for c in s:
            alpha1[c] = 1 + alpha1.get(c,0)
        for c in t:
            alpha2[c] = 1 + alpha2.get(c,0)
        return alpha1 == alpha2
        