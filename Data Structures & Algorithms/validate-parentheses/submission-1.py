class Solution:
    def isValid(self, s: str) -> bool:
        paranth_map = {"{":"}","(":")","[":"]"}
        stack =[]
        for char in s:
            if char in paranth_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                if paranth_map[stack[-1]]==char:
                    stack.pop()
                else:
                    return False
        return len(stack)==0