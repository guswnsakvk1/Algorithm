"""
전공평점 : 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값

입력값 : A+,A0,B+,B0,C+,C0,D+,D0,F,P
※ P는 과목 계산에서 제외해야 함
"""

answer = 0
num = 0
subject_ratings = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, 
                   "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0,
                  "F" : 0.0}

for i in range(20):
  subject, credit, rating = input().split()

  if rating != "P":
    answer += float(credit) * subject_ratings[rating]
    num += float(credit)
    
print(round(answer / num, 6))