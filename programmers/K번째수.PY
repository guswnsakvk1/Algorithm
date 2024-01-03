def solution(array, commands):
    answer = []
    for command in commands:
        newArray = sorted(array[command[0]-1:command[1]])
        answer.append(newArray[command[2]-1])
        
    return answer