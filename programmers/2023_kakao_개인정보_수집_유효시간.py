## 처음에는 12줄에 while문이 아니라 단순히 if문만을 사용했다.
## if문을 사용하니 m 0이 나오는 오류가 발생
## while문을 사용해서 m이 13보다 클 경우에만 12을 빼도록 함

def solution(today, terms, privacies):
    answer = []
    terms_list = {}
    for term in terms:
        terms_list[term[0]] = int(term.split(" ")[-1])
    
    for i in range(len(privacies)):
        y, m, d = map(int, privacies[i].split(" ")[0].split("."))
        m += terms_list[privacies[i][-1]]
        while m > 12:
            m -= 12
            y += 1
        storage_date = str(y) + "." + str(m).rjust(2,"0") + "." + str(d).rjust(2,"0")
        if today >= storage_date:
            answer.append(i+1)
        
    return answer