def solution(numbers, hand):
    pad = {1 : [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6: [1,2],
          7: [2,0], 8: [2,1], 9: [2,2], 0: [3,1] }
    answer = ''
    left = [3,0]
    right = [3,2]
    
    for number in numbers:
        if number % 3 == 1:
            answer += 'L'
            left = pad[number]
        elif number % 3 == 0 and number != 0:
            answer += 'R'
            right = pad[number]
        else:
            left_len = abs(pad[number][0] - left[0])  + abs(pad[number][1] - left[1]) 
            right_len = abs(pad[number][0] - right[0]) + abs(pad[number][1] - right[1])
            
            if left_len < right_len:
                answer += 'L'
                left = pad[number]
            elif left_len > right_len:
                answer += 'R'
                right = pad[number]
            else:
                if hand == "left":
                    answer += 'L'
                    left = pad[number]
                else:
                    answer += 'R'
                    right = pad[number]

    return answer