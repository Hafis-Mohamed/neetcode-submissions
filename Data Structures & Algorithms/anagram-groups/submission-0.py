class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=[]
        dict=defaultdict(list)
        for str in strs:
            key=" ".join(sorted(str))
            dict[key].append(str)
        for key in dict:
            anagram.append(dict[key])
        return anagram

            
        