class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        s=''
        for i in digits:
            s=s+str(i)

        k=int(s)+1

        ss=str(k)

        val=[]
        for i in ss:
            val.append(int(i))

        return val
