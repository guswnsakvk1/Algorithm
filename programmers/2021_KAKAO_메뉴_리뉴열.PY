import itertools

def solution(orders, course):
    answer = []
    orders_sort = []
    menus = {}
    ## AB와 BA는 같은 메뉴로 보기때문에
    ## 값을 알파벳순서대로 정렬
    for i in orders:
        lst = list(i)
        lst.sort()
        orders_sort.append("".join(lst))
    
    ## course 리스트 안에 있는 값보다 작은 경우
    ## 코스요리를 못만들기에 j값보다 작은 경우 break
    ## j보다 값이 큰 경우 조합을 이용해서 모든 경우의 수 구하기
    for i in orders_sort:
        for j in course:
            if len(i) < j:
                break
                
            lst = itertools.combinations(i, j)
            for k in lst:
                key = "".join(k)
                if key in menus:
                    menus[key] += 1
                else:
                    menus[key] = 1
    
    ## menus 안에 있는 값을 key의 길이, value의 순서대로 정렬
    ## key의 길이의 순서대로 value의 순서대로 값을 비교해서 정답을 구하기 위함
    menus = sorted(menus.items(), key=lambda x: (len(x[0]), x[1]))
    
    lst = []
    ## menus의 value값과 비교할 변수
    order_time = 1
    ## menus의 key값의 길이를 비교할 변수
    name = course.pop(0)
    
    for menu in menus:
        ## value값이 1이면 정답이 아예 안되므로 continue
        if menu[1] == 1:
            continue
        else:
            ## menu[0]가 name보다 길다면 무조건
            ## lst의 값은 정답이므로 answer에 값넣기
            if name < len(menu[0]):
                answer += lst
                order_time = 1
                name = course.pop(0)
                lst = []
            
            ## value값이 order_time고 같다면 lst에 넣기
            ## 아닐경우 lst를 [menu[0]]으로 바꾸기
            if order_time == menu[1]:
                lst.append(menu[0])
            else:
                order_time = menu[1]
                lst = [menu[0]]
    
    ## 마지막 길이의 lst는 answer에 못 들어갔으므로
    ## order_time이 1보다 큰 경우 answer에 넣기
    if order_time > 1:
        answer += lst
    
    ## 정답은 사전식으로 출력하기에 정렬
    answer.sort()
    
    return answer