"""
문자를 치환하는 이유
: C#, D#, F#, G#, A#을 하나의 문자로 봐야하기에

1. 치환할 문자를 리스트로 만들기

2. m을 치환하기

3. musicinfos의 요소를 ',' 기준으로 나누기
: start(시작하는 시간), end(끝나는 시간), title(제목), music(노래)

4. music 요소 치환하기

5. 음악이 연주되는 시간(gap) 구하기

6. music이 얼마나 반복될 수 있는지 구해서 music 다시 만들기

7. m이 music에 있고 gap이 time보다 크면 answer, time 업데이트
"""

def solution(m, musicinfos):
    tmp = ['C#', 'D#', 'F#', 'G#', 'A#']
    answer = '(None)'
    time = 0
    
    for i, key in enumerate(tmp):
        m = m.replace(key, str(i))
        
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        
        for i, key in enumerate(tmp):
            music = music.replace(key, str(i))
            
        start_hour, start_minute = map(int, start.split(':'))
        end_hour, end_minute = map(int, end.split(':'))
        
        gap = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)
        
        repeat, rest = divmod(gap, len(music))
        music = music * repeat + music[:rest]
        
        if m in music and gap > time:
            time = gap
            answer = title
    
    return answer