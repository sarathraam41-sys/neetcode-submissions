class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        freq1={}
        for c in s:
            freq[c]=freq.get(c,0)+1
        for ch in t:
            freq1[ch]=freq1.get(ch,0)+1
        if freq == freq1:
            return True
        else:
            return False
        
        