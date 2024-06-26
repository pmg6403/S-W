'''
    작성일 : 2024년 3월 28일
    작성자 : 컴퓨터 공학부 202495005 박민규
    설명 : 정수를 입력받아 음수인지 양수인지 판단하시오.

    [문제분석]
        필요한 변수는 무엇? num(입력받은 숫자)
        숫자를 입력 받는다
        0점 이상인가?
        아닌가?
        입력받은 숫자가 음수인지 양수인지 판단한다.
        입력받는 숫자는 반드시 정수로 변환해야 한다.
        
        
    [알고리즘]
        1. 숫자를 입력 받는다.
        2. 만약 정수가 0보다 크면
            2-1. 0보다 크면 "양수입니다." 츌력한다.
        3. 아니고 만약 정수가 0보다 작으면
            3-1 0보다 직으면 "음수입니다." 출력한다
        4. 아니면
            4-1 0입니다.
        5. "감사합니다." 출력한다.
            => 조건과 상관없이 무조건 출력
'''
# 1. 정수를 입력받는다.
num = int(input("숫자 입력 : "))

# 2. 만약 정수가 0보다 크면 (양수인가?)
if num > 0 :
    print("양수입니다.")
    
# 3. 아니고 만약
elif num < 0 :
    print("음수입니다.")

else : # 나머지는.. 절대로 조건식을 작성하지 않는다.
    print("0입니다.")

# 4. "프로그램 종료"를 출력한다.    
print("프로그램 종료")