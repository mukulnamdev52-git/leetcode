class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        
        # Step 1: Remove non-alphanumeric and convert to lowercase
        for char in s:
            if char.isalnum():
                cleaned += char.lower()


        
        # Step 2: Check if palindrome
        return cleaned ==cleaned[::-1]

            
        