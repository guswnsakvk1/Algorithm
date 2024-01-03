"""
1. '('이면 tmp에 2곱하기, '['이면 tmp에 3곱하기

2. ')'이면 
1) stack이 비지않고 stack[-1]이 '['이면
   올바른 괄호열이 아니기에 answer = 0
2) 만약 s[i-1]이 '('이면 answer에 tmp 더하기
3) stack.pop()
4) tmp 나누기 2

3. ']'이면 
1) stack이 비지않고 stack[-1]이 '('이면
   올바른 괄호열이 아니기에 answer = 0
2) 만약 s[i-1]이 '('이면 answer에 tmp 더하기
3) stack.pop()
4) tmp 나누기 3

4. 만약 스택이 
1) 있으면 0출력
2) 없으면 answer 출력

※ 곱하기 법칙을 생각하면 접근하기 쉬움
(()[])
-> 2랑 3을 더하고 2를 곱한다
-> 2에 2곱한 것과 3에 2곱한 것을 더한다
"""

s = list(input())

stack = []
tmp =1
answer = 0

for i in range(len(s)):
  if s[i] == '(':
    stack.append(s[i])
    tmp *= 2
  elif s[i] == '[':
    stack.append(s[i])
    tmp *= 3
  elif s[i] == ')':
    if not stack or stack[-1] == '[':
      answer = 0
      break
    if s[i-1] == '(':
      answer += tmp

    stack.pop()
    tmp //= 2
  else:
    if not stack or stack[-1] == '(':
      answer = 0
      break
    if s[i-1] == '[':
      answer += tmp

    stack.pop()
    tmp //= 3

if stack:
  print(0)
else:
  print(answer)