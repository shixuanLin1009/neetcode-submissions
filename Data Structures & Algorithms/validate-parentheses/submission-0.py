
class Solution:
    def isValid(self, s: str) -> bool:
        close2open = {")":"(","}":"{","]":"["}
        stack=[]
        for c in s:
            if c in close2open:
                if stack and stack[-1]==close2open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack