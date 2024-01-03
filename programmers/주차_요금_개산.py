import math

def solution(fees, records):
    parking = dict()
    stack = dict()
    
    for record in records:
        time, car, move = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute)
        
        if move == "IN":
            parking[car] = minutes
        elif move == "OUT":
            try:
                stack[car] += minutes - parking[car]
            except:
                stack[car] = minutes - parking[car]
            del parking[car]
            
    for car, minute in parking.items():
        try:
            stack[car] += 23 * 60 + 59 - minute
        except:
            stack[car] = 23 * 60 + 59 - minute
            
    a = dict(sorted(stack.items()))
    answer = []
    for car, minute in a.items():
        fare = fees[1] + math.ceil(max(0, minute - fees[0]) / fees[2]) * fees[3]
        answer.append(fare)
    
    return answer