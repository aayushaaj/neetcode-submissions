class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res=[]
        for s in strs:
            res.append(str(len(s))+'|'+s)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result=[]
        i=0
        while(i<len(s)):
            j=i
            while s[j]!='|':
                j+=1
            length=int(s[i:j]) 
            result.append(s[j+1:length+j+1])
            i=length+j+1
       
        return result

       

    
