def checkBalancedParenthesis(s):
    stack = []
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    if (len(s) == 0):
        raise TypeError
    else:
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if stack and stack[-1] == matching_brackets[char]:
                    stack.pop()
                else:
                    return 'Unbalanced'
        if stack:
            return "Unbalanced"
        return "Balanced"

def getUnbalancedPositions(s):
    stack = []
    unbalanced_positions = []
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    if (len(s) == 0):
        raise TypeError
    for i, char in enumerate(s):
        if char in '([{':
            stack.append((char, i))
        elif char in ')]}':
            if stack and stack[-1][0] == matching_brackets[char]:
                stack.pop()
            else:
                unbalanced_positions.append(i)

    while stack:
        unbalanced_positions.append(stack.pop()[1])
    unbalanced_positions.sort()
    return unbalanced_positions

try:
    '''
    expression = "a + (b * c) - {d / e}"
    print(expression, ":", checkBalancedParentheses(expression))
    expression = "a + (b * c] - {d / e)"
    print(expression, ":", checkBalancedParentheses(expression))
    expression = "()(()){([()])}"
    print(expression, ":", checkBalancedParentheses(expression))
    expression = "((()(()){([()])}"
    print(expression, ":", checkBalancedParentheses(expression))
    expression = ")(()){([()])}"
    print(expression, ":", checkBalancedParentheses(expression))
    expression = "({[])}"
    print(expression, ":", checkBalancedParentheses(expression))
    expression = ""
    print(expression, ":", checkBalancedParentheses(expression))
    '''

    results = []
    expression = "(]"
    print(expression, ":", getUnbalancedPositions(expression))

    expression = "(a+b"
    print(expression, ":", getUnbalancedPositions(expression))

    expression = "a + (b * c] - {d / e)"
    print(expression, ":", getUnbalancedPositions(expression))

    expression = "a + (b * c) - {d / e}"
    print(expression, ":", getUnbalancedPositions(expression))

    expression = ""
    print(expression, ":", getUnbalancedPositions(expression))

except TypeError:
    print("Input string can't be empty")
