def solution(answers):
    answer = []
    student_score = [0,0,0]
    student_num = [0,0,0]
    student_1_pattern = [1,2,3,4,5]
    student_2_pattern = [2,1,2,3,2,4,2,5]
    student_3_pattern = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        student_num[0] = i % 5
        student_num[1] = i % 8
        student_num[2] = i % 10
        
        if(answers[i] == student_1_pattern[student_num[0]]): student_score[0] += 1
        if(answers[i] == student_2_pattern[student_num[1]]): student_score[1] += 1
        if(answers[i] == student_3_pattern[student_num[2]]): student_score[2] += 1
    
    max_score = max(student_score)
    for i in range(3):
        if student_score[i] == max_score:
            answer.append(i+1)
        
    return answer