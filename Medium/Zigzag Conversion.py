class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        # Because there is not efficient numbers of charecters.

        rows=['']*numRows #This will crearte required numbers of row for the charecters.
        current_row=0 # tracking row real-time
        going_down=False #it will help to decide either we will go upper or down row.

        for char in s:#going through the string
            rows[current_row]+=char #update the charecter into the different row 

            if current_row==0 or current_row==numRows-1:
                going_down= not going_down #specify condition for up or down in between rows
            current_row+=1 if going_down else -1 #updating the condition
        return ''.join(rows)

