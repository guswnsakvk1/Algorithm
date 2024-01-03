## 괄호의 짝이 맞아야하기에 stack에 괄호의 시작을 넣기
## 현재 괄호가 괄호의 끝부분일 경우 stack의 마지막과 비교해서 짝이 맞으면 진행 아니면 break
## 괄호의 시작: '[', '(', '{'
## 괄호의 끝부분 : ']', ')', '}'
def solution(s):
    answer = 0
    stack = []
    flag = True
    
    for i in range(len(s)):
        for j in range(len(s)):
            if s[j] == '[' or s[j] == '{' or s[j] == '(':
                stack.append(s[j])
            elif stack:
                if s[j] == ']' and stack[-1] == '[':
                    stack.pop()
                elif s[j] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[j] == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        
        ## stack에 요소가 남아있을 경우 짝이 없는 괄호가 있기에 not stack
        if not stack and flag:
            answer += 1
        s = s[1:] + s[0]
        flag = True
                
    
    return answer