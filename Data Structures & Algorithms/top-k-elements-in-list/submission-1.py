class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # mydict=defaultdict(int)
        # result=[]
        # for i in range(len(nums)):
        #     mydict[nums[i]]+=1
        # s=dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
  
        # res=list(s.keys())
        # return res[:k]
    # HEAP

        count = {}
        res=[]
        for num in nums:
            count[num]=1+count.get(num,0)
        heap=[]
        for key, val in count.items():
            heapq.heappush(heap,(val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        return res

       
            
    
         
            
            

