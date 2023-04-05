def balanced_brackets(my_string: str):
    # Base case: an empty string is always balanced
    if not my_string:
        return True
    
    # Remove non-bracket characters
    my_string = ''.join(c for c in my_string if c in '()[]')
    
    # Check if the string starts with an opening bracket and ends with a closing bracket of the same type
    if my_string[0] == '(' and my_string[-1] == ')' or my_string[0] == '[' and my_string[-1] == ']':
        # Find the index of the matching closing bracket
        count = 0
        for i in range(1, len(my_string)-1):
            if my_string[i] == '(' or my_string[i] == '[':
                count += 1
            elif my_string[i] == ')' or my_string[i] == ']':
                count -= 1
            
            # If the matching closing bracket is found, recursively call the function on the substring inside the outer brackets
            if count == -1:
                return balanced_brackets(my_string[1:i]) and balanced_brackets(my_string[i+1:-1])
    
    # If the string doesn't start with an opening bracket or the closing bracket doesn't match, it's not balanced
    return False
