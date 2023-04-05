def balanced_brackets(my_string: str):
    def helper(s: str, stack: list):
        if not s:
            return not stack

        char = s[0]

        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack or (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '['):
                return False
            stack.pop()

        return helper(s[1:], stack)

    return helper(my_string, [])

