from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map sorted_string -> list of original strings
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a unique key
            # sorted('eat') returns ['a', 'e', 't'], so we join it back
            sorted_key = "".join(sorted(s))
            
            # Group the original string under its sorted key
            anagram_map[sorted_key].append(s)
            
        # Return just the grouped lists
        return list(anagram_map.values())