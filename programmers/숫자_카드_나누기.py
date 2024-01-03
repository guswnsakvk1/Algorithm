import math
from collections import deque

## 최대공약수 구하는 함수
def GCD(lst):
    dq = deque(lst)
    for i in range(len(lst)-1):
        num = math.gcd(dq.popleft(), dq.popleft())
        dq.appendleft(num)
        
    return dq[0]

## 최대공약수의 약수를 구하는 함수
def getMyDivisor(n):
    divisorsList = []

    ## 루트를 활용
    ## 숫자의 반까지 나누어 떨어지는 숫자를 구하고
    ## 떨어지는 숫자를 주어진 최대공약수에 나누어서 짝꿍구하기 
    for i in range(2, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    ## 최대공약수 본인이 빠지므로 추가
    divisorsList.append(n)
    
    return divisorsList

## 답을 도출하는 함수
def getAnser(listA, listB, arrayA, arrayB):
    numA, numB = 0, 0
    for i in range(len(listA)-1, -1, -1):
        flag = True
        for j in arrayB:
            if j % listA[i] == 0:
                flag = False
                break
                
        if flag == True:
            numA = listA[i]
            break
            
    for i in range(len(listB)-1, -1, -1):
        flag = True
        for j in arrayA:
            if j % listB[i] == 0:
                flag = False
                break
                
        if flag == True:
            numB = listB[i]
            break
            
    return max(numA, numB)

def solution(arrayA, arrayB):
    listA = []
    listB = []
    
    numA = GCD(arrayA)
    numB = GCD(arrayB)
    
    listA = getMyDivisor(numA)
    listB = getMyDivisor(numB)
            
    answer = getAnser(listA, listB, arrayA, arrayB)
    
    return answer