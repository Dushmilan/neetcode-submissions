class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        have = 0
        required = len(need)

        left = 0
        best_left = 0
        best_len = float("inf")

        for right, char in enumerate(s):

            # Add character to window
            if char in need:
                window[char] = window.get(char, 0) + 1

                # This character just satisfied its requirement
                if window[char] == need[char]:
                    have += 1

            # Window is valid
            while have == required:

                # Update minimum window
                current_len = right - left + 1

                if current_len < best_len:
                    best_len = current_len
                    best_left = left

                # Remove leftmost character
                left_char = s[left]

                if left_char in need:
                    window[left_char] -= 1

                    # Window is no longer satisfying this character
                    if window[left_char] < need[left_char]:
                        have -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_left:best_left + best_len]