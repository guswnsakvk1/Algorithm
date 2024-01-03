def solution(name):
    ## name 길이
    name_len = len(name)
    ## 움직인 횟수 저장하는 변수
    move = 1e9
    ## 입력된 name 왼쪽에 있는 'A'가 아닌 글자 위치 저장
    left = []
    ## 입력된 name 오른쪽에 있는 'A'가 아닌 글자 위치 저장
    right = []
    ## 글자 가운데 위치
    mid = (len(name) - 1) // 2

    ## 글자를 얼마나 바꿔야 하는지 입력
    change = 0

    for i in range(len(name)):
        ## 현재 글자가 'A'가 아니면 change에 얼마나 버튼을 눌러야하는지 저장
        if name[i] != 'A':
            change += min(ord(name[i]) - 65, ord('Z') - ord(name[i]) + 1) 

            ## mid 보다 왼쪽이면 left에 오른쪽이면 right에 위치 저장
            if i > mid:
                right.append(i)
            ## i는 무조건 처음에 변경하면 되기에 위치 기록안해도 됨
            elif i != 0:
                left.append(i)


    ## left, right가 name 길이와 같다면 move는 글자 길이 - 1
    if len(left) + len(right) == name_len:
        move = name_len - 1
    ## left, right가 없는 경우 move 0
    elif not left and not right:
        move = 0
    ## left는 없고 right만 있는 경우 <- 만 입력해서 움직임
    elif not left and right:
        move = name_len - right[0]
    ## right는 없고 left만 있는 경우 -> 입력해서 뒤에서 움직임
    elif left and not right:
        move = left[-1]
    ## left, right 둘다 있을 경우
    ## 1. 오른쪽으로 갔다가 왼쪽으로 가는 경우 : left[-1] + ((name_len - right[0]) * 2)
    ## 2. 왼쪽으로 갔다가 왼쪽으로 가는 경우 : (left[-1] * 2) + name_len - right[0]
    ## 3. 왼쪽만 가는 경우 : right[-1], name_len - left[0]
    ## 4. 오른쪽으로만 가는 경우 : right[-1]
    elif left and right:
        move = min((left[-1] * 2) + name_len - right[0], left[-1] + ((name_len - right[0]) * 2), right[-1], name_len - left[0])

    ## move가 name 길이보다 작으면 move에 change 더해서 리턴
    ## 아니면 name 길이에 change 더해서 리턴
    if move < name_len:
        return move + change
    else:
        return name_len + change