class Solution:
    def reverse(self, x: int) -> int:
        li=['0', '-']
        out=list(str(x))
        res=0
        if out[0]=='0':
            k=out[::-1]
            result=''.join(k[:len(k)])
            d= int(result)
        elif out[0]=='-':
            k=out[::-1]
            result=''.join(k[:len(k)-1])
            print(result)
            res= -int(result)
        else:
            k=out[::-1]
            result=''.join(k)
            res= int(result)
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res
        #alhamdulliah i did