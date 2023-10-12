class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        lst=[]
        first=0
        for i in spaces:
           lst.append(s[first:i])
           first=i
        lst.append(s[first:])
        joined=' '.join(lst)
        return joined
