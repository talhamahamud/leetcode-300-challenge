class Solution:
    def reverseVowels(self, s: str) -> str:
        vow=set('aeiouAEIOU')
        s=list(s)

        left=0
        right=len(s)-1

        while left<right:
            if s[left] in vow and s[right] in vow:
                s[left], s[right]=s[right], s[left]
                left+=1
                right-=1

            elif s[left] in vow and s[right] not in vow:
                right-=1

            elif s[left] not in vow and s[right] in vow:
                left+=1

            else:
                left+=1
                right-=1
        return "".join(s)