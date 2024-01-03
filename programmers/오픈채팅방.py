def solution(record):
    answer = []
    ## 어떤 유저가 들어왔는데 나갔는지 저장하는 리스트
    logs = []
    ## 유저 아이디와 닉네임 저장하는 dict
    user = {}
    
    for log in record:
        log = log.split(" ")
        if log[0] == 'Enter':
            logs.append((log[1], "님이 들어왔습니다."))
            user[log[1]] = log[2]
        elif log[0] == 'Leave':
            logs.append((log[1], "님이 나갔습니다."))
        else:
            user[log[1]] = log[2]
    
    for user_id, state in logs:
        answer.append(user[user_id] + state)
    
    return answer