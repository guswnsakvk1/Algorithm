def solution(s):
    stack = []

    for i in range(len(s)):
        if(s[i] == "("):
            stack.append("(")
        elif(stack and s[i] == ")"):
            stack.pop()
        else:
            return False
            
    if(stack):
        return False

    return True