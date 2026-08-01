class Solution(object):
    def isValid(self, s):
        stack = []

        matching = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        for ch in s:
            if ch in '[{(':
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                top = stack.pop()

                if matching[ch] != top:
                    return False

        return len(stack) == 0
                
        