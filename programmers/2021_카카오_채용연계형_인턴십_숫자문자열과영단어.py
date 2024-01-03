def solution(s):
    lst = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(lst)):
        s = s.replace(lst[i], str(i))

    return int(s)