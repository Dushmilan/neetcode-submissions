class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Track minimum at each level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Store current minimum alongside each push
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            # If we removed the minimum, update min_stack
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]  # O(1) - just look at top