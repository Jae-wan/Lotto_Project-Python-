'''
1. 번호 합 범위 필터
 - rand() 번호 추출 (단, 범위는 1~45까지이되, 중복은 제거)
 - 일정 번호의 범위 합을 넘어서면 재 추출 (원하는 범위까지만 추출)
            * 충족 조건 3가지 *
        - MAX 보다 이하인가?
        - MIN 보다 이상인가?
        - MIN < 값 < MAX 인가?
'''





import random

print(random.randrange(1,45))
# random.randrange(start, end, step)
# start 부터 end 까지 정수 난수 생성

rand_NUMBER = []    # 난수 저장 List
number_MAX_RANGE=80 # 번호 합 MAX 값
sum_randNUMBER=0    # sum() 으로 1차원 리스트 값 합치기
switch_while=0

while(1):
    for i in range(0, 7, 1):
        set_NUMBER = random.randrange(1,45)     # set_NUMBER 변수에 난수 추출
        rand_NUMBER.append(set_NUMBER)          # 추출된 난수를 rand_NUMBER List에 끼워넣음

    sum_randNUMBER=sum(rand_NUMBER)
        # rand_NUMBER 리스트의 1차원 값들을 모두 합쳐서 sum_randNUMBER 에 저장
    if(sum_randNUMBER < number_MAX_RANGE):
        print("저장 된 값/합계 : " + str(rand_NUMBER) + "/" + str(sum_randNUMBER))
        # 엑셀에도 저장 해야함.
        switch_while+=1
        if(switch_while==1):
            break
    else:
        print("건너뛰어진 값/합계 : " + str(rand_NUMBER) + "/" + str(sum_randNUMBER))
        rand_NUMBER=[]
        sum_randNUMBER=0    #sum및 LIST 한번 초기화





