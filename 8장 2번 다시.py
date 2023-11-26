#사용자로부터 10진 양의 정수를 입력받아 각 자릿수를 한글로 표시해주는 프로그램

def read_single_digit(d):
    digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return digits[int(d)]

def read_number(num):
    n= str(num) #숫자를 문자열로 변환하기

    for d in n:
        print(read_single_digit(d), end= ' ')
        

num=int(input('양의 정수 입력:'))

read_number(num)


    

