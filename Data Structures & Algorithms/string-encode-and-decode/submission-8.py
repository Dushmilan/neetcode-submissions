class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded=""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Find the delimiter
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            # Get the length
            length = int(s[i:j])
            # Extract the string
            result.append(s[j+1:j+1+length])
            i = j + 1 + length
        return result