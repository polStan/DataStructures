def checkBalancedParenthesis(s):
    if not s:
        raise TypeError

    stack = []
    opening = {'(': ')', '[': ']', '{': '}'}
    closing = {')', ']', '}'}

    for char in s:
        if char in opening:
            stack.append(opening[char])
        elif char in closing:
            if not stack or stack.pop() != char:
                return "Unbalanced"
        
    if not stack:
        return "Balanced" 
    else:
        return "Unbalanced"









def checkUnbalancedParenthesis(s):
    if not s:
        return 