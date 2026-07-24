class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_actions = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)  # Truncate toward zero
        }
        stack = []

        for char in tokens:
            if char not in operator_actions:
                stack.append(int(char))  # Convert to int immediately
            else:
                y = stack.pop()  # Right operand (top)
                x = stack.pop()  # Left operand (second from top)
                ans = operator_actions[char](x, y)
                stack.append(ans)
        
        return stack[0]