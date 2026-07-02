class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        paranth_dict = {'(':')','{':'}','[':']'}
        stack = []
        
        for char in s:
            if char in paranth_dict:  # Opening bracket
                stack.append(char)
            else:  # Closing bracket
                if not stack:  # No opening bracket to match
                    return False
                last_open = stack.pop()  # ✅ Only runs for closing brackets
                if paranth_dict[last_open] != char:
                    return False
        
        return len(stack) == 0