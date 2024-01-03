## 맨 뒤에 있는 숫자보다 작고 앞 숫자보다 큰 숫자가 오면 안될거라고 생각해서
## stack을 사용하는 것이 아니라고 생각했으나
## 1 3 2가 입력이라고 친다면 stack에 있는 마지막 숫자만 비교해도 답을 도출해낼 수 있다고 확인되어
## stack을 사용해서 품

def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
        
    return answer