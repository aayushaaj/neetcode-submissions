class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict=defaultdict(int)
        result=[]
        for i in range(len(nums)):
            mydict[nums[i]]+=1
        s=dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
  
        res=list(s.keys())
        return res[:k]
    
            
            

