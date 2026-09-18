class Solution:

    
    def isValid(self, s: str) -> bool:
        openBrackets, endBrackets = ['(', '[', '{',], ['}', ']', ')']
        bracketStack = []

        def checkValidity(char, bracket):
            if (char == '}' and bracket != '{') or (char == ']' and bracket != '[') or (char == ')' and bracket != '('):
                return False
            
            return True

        for c in s:
            if c in openBrackets:
                bracketStack.append(c)
            else:
                if len(bracketStack) == 0: return False
                openBracket = bracketStack.pop()
                valid = checkValidity(c, openBracket)
                if not valid: return False
        
        return len(bracketStack) == 0