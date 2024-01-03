def solution(record):
    answer = []
    user = {}
    
    for logs in record:
        log = logs.split(" ")
        if log[0] == 'Enter':
            answer.append(log[1] + "님이 들어왔습니다.")
            user[log[1]] = log[2]
        elif log[0] == 'Leave':
            answer.append(log[1] + "님이 나갔습니다.")
        else:
            user[log[1]] = log[2]
    
    for i in range(len(answer)):
        for key, value in user.items():
            if key in answer[i]:
                answer[i] = answer[i].replace(key, value)
                continue
    
    return answer