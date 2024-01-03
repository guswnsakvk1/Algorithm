import sys
input = sys.stdin.readline

n = int(input())

# 중복제거
# 피는 시기가 같은 경우 가장 늦게 지는 꽃만 남기기
flower = {}
for _ in range(n):
    start_month, start_day, end_month, end_day = map(int, input().split())

    try:
        if flower[str(start_month).zfill(2) + str(start_day).zfill(2)] < str(end_month).zfill(2) + str(end_day).zfill(2):
            flower[str(start_month).zfill(2) + str(start_day).zfill(2)] = str(end_month).zfill(2) + str(end_day).zfill(2)
    except:
        flower[str(start_month).zfill(2) + str(start_day).zfill(2)] = str(end_month).zfill(2) + str(end_day).zfill(2)

# 먼저 피는 순서대로 정렬
flower = dict(sorted(flower.items(), key=lambda item:item))

# 현재 꽃 피는 시기
start_flower = ''
# 현재 꽃 지는 시기
end_flower = ''
# 임시 꽃 피는 시기
keep_start_flower = ''
# 임시 꽃 지는 시기
keep_end_flower = ''
# 3월 1일전에 피는 꽃을 저장하는 리스트
lst = []
answer = 0

for start, end in flower.items():
    # 현재 꽃을 안정해졌을 경우
    if start_flower == '':
        # 만약 start가 3월1일 보다 작거나 같을 경우
        # lst에 피는 시기, 지는 시기 넣기
        if start <= '0301':
          lst.append((start, end))
          continue
        # 3월 1일 보다 클 경우
        else:
            # 만약 lst가 있다면
            if lst:
                # lst를 지는 순서대로 정렬하기
                lst.sort(key=lambda x:x[1])
                # lst의 마지막 값의 피는 시기
                # start_flower에 저장
                start_flower = lst[-1][0]
                # lst의 마지막 값의 지는 시기
                # end_flower에 저장
                end_flower = lst[-1][1]
                # answer에 1더하기
                answer += 1
            # 만약 lst가 없다면
            else:
                # 답이 없는 경우이므로 0출력
                print(0)
                # 프로그램 종료
                exit()

    # 만약 현재 꽃의 피는 시기가 start보다 더 클 경우
    if end_flower > start:
        # 만약 임시 꽃이 없다면
        if keep_start_flower == '':
            # 임시 꽃 피는 시기 저장
            keep_start_flower = start
            # 임시 꽃 지는 시기 저장
            keep_end_flower = end
            # 계속 진행
            continue
        # 만약 임시 꽃이 있다면
        else:
            # 만약 임시 꽃의 지는 시기가
            # end보다 작으면
            if keep_end_flower < end:
                # 임시 꽃 피는 시기 start로 변경
                keep_start_flower = start
                # 임시 꽃 지는 시기 end로 변경
                keep_end_flower = end
    # 만약 현재 꽃의 지는 시기가 start와 같을 경우
    elif end_flower == start:
        # 만약 임시 꽃이 없다면
        if keep_start_flower == '':
            # 현재 꽃 피는 시기 start로 변경
            start_flower = start
            # 현재 꽃 지는 시기 end로 변경
            end_flower = end
            # answer에 1더하기
            answer += 1
        # 만약 임시 꽃이 있으면
        else:
            # 만약 임시 꽃 지는 시기가
            # end보다 크거나 같을 경우
            if keep_end_flower >= end:
                # 현재 꽃 피는 시기 임시 꽃 피는 시기로 변경
                start_flower = keep_start_flower
                # 현재 꽃 지는 시기 임시 꽃 지는 시기로 변경
                end_flower = keep_end_flower
            # end가 더 클 경우
            else:
                # 현재 꽃 피는 시기 start로 변경
                start_flower = start
                # 현재 꽃 지는 시기 end로 변경
                end_flower = end
            # 임시 꽃 초기화
            keep_start_flower = ''
            keep_end_flower = ''
            # answer 더하기 1
            answer += 1
    # 만약 현재 지는 시기보다 start가 클 경우
    else:
        # 만약 임시 꽃이 없다면
        if keep_end_flower == '':
            # 답이 없으므로 0출력
            print(0)
            # 프로그램 종료
            exit()
        # 임시 꽃이 있다면
        else:
            # 만약 임시 꽃 지는 시기가 start보다 크거나 같을 경우
            if keep_end_flower >= start:
                # 현재 꽃 피는 시기 임시 꽃 피는 시기로 변경
                start_flower = keep_start_flower
                # 햔제 꽃 지는 시기 임시 꽃 지는 시기로 변경
                end_flower = keep_end_flower
                # 임시 꽃 피는 시기 start로 변경
                keep_start_flower = start
                # 임시 꽃 지는 시기 end로 변경
                keep_end_flower = end
                # answer에 1 더하기
                answer += 1
            # 임시 꽃 지는 시기가 start 보다 작으면
            else:
                # 반복문 탈출
                break

print(flower)
print(end_flower)
print(keep_end_flower)

# 현재 꽃 지는 시기가 11월30일 보다 크면
# answer 출력
if end_flower > '1130':
    print(answer)
# 지는 꽃 지는 시기가 11월30일 보다 크면
# answer에 1더하고 출력
elif keep_end_flower > '1130':
    print(answer+1)
# 아니면 0 출력
else:
    print(0)