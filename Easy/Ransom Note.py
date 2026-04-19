class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Optimization: If the note is longer than the magazine, it's impossible
        if len(ransomNote) > len(magazine):
            return False
        
        # Count characters in magazine
        counts = {}
        for char in magazine:
            counts[char] = counts.get(char, 0) + 1
            
        # Check against ransomNote
        for char in ransomNote:
            if char not in counts or counts[char] <= 0:
                return False
            counts[char] -= 1
            
        return True