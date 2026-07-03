class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(str(len(s))+'|'+s)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while(i<len(s)):
            # if s[i].isdigit() and s[i+1]=='|':
            j=i
            while s[j]!='|':
                j+=1
            length=int(s[i:j]) 
            result.append(s[j+1:length+j+1])
            i=length+j+1
       
        return result

    
