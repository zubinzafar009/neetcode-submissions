class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen.values():
                stack.append(c)
            else:
                if len(stack) > 0 and stack.pop() == closeToOpen[c]:
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

        