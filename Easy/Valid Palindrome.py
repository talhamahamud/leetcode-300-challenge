import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(cleaned_string)
        if cleaned_string.lower()==cleaned_string[::-1].lower():
            return True
        else:
            return False
# so what's the slolution, firstly remove all the non-alphanumeric
# then find out that, is it palindromic or not
# but all the charecter should be either upper or lower case.
        