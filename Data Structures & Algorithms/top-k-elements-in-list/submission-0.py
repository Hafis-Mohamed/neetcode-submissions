class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        result=[]
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        sorted_dict=sorted(dict.items(), key=lambda x: x[1], reverse=True)        
        for key,val in sorted_dict[:k]:
            result.append(key)
        return result
        