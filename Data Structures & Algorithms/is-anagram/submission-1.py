class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        seen={}
        for ss in s:
            if ss in seen:
                seen[ss]+=1
            else:
                seen[ss]=1
        for ss in t:
            if ss not in seen:
                return False
            else:
                seen[ss]-=1
                if seen[ss]==0:
                    del seen[ss]
        if seen:
            return False
        else:
            return True