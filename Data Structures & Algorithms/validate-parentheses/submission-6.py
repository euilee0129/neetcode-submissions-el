class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        if '(' not in s and '[' not in s and '{' not in s:
            return False
        stack = []
        for c in s:
            if c == '(' or c== '[' or c=='{':
                stack.append(c)
            elif c == ')'and len(stack) >0:
                popped = stack.pop()
                if popped != '(':
                    return False
            elif c== ']'and len(stack) >0:
                popped = stack.pop()
                if popped != '[':
                    return False
            elif c=='}'and len(stack) > 0:
                popped = stack.pop()
                if popped != '{':
                    return False
            else:
                return False

        return len(stack) == 0

            
        