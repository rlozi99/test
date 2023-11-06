# format 함수로 숫자를 문자열로 변환
# 앞쪽에 있는 문자열을 {}기호가 format() 함수 괄호 안에 있는 매개변수로 차례로 대치되면서 숫자가 문자열이 되는 것
"""str_a = "{}".format(10)
print(str_a)
print(type(str_a))

"""

"""format_a = "{}만원".format(5000)
format_b = "연봉 {}만원 만들기".format(8000)
format_c = "{} {} {}".format(300, 5, 20)
format_d = "{} {} {}".format(1, "문자", True)
format_e = "{}".format(True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)
print(type(format_e))"""

"""output_a = "{:d}".format(52)     #정수를 출력하겠다고 직접적으로 지정

#특정 칸에 출력
output_b = "{:5d}".format(52)       #5칸을 빈칸으로 잡고 출력
output_c = "{:10d}".format(52)      #10칸을 빈칸으로 잡고 출력

#빈칸을 0으로 채우기
output_d = "{:05d}".format(52)      
output_e = "{:05d}".format(-52)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)
"""

"""output_h = "{:+5d}".format(52)       #기호를 뒤로 밀기
output_i = "{:+5d}".format(-52)
output_j = "{:=+5d}".format(52)         #기호를 앞으로 밀기
output_k = "{:=+5d}".format(-52)
output_l = "{:+05d}".format(52)         #앞을 0으로 채우기
output_m = "{:+05d}".format(-52)

print(output_h)
print(output_i) 
print(output_j)
print(output_k)
print(output_l)
print(output_m)"""
"""
output_a = "{:f}".format(12.552)
output_b = "{:10f}".format(12.552)
output_c = "{:15f}".format(12.552)
output_d = "{:+15f}".format(12.552)
output_e = "{:+015f}".format(12.552)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)"""
"""
output_a = "{:0.3f}".format(12.552)
output_b = "{:10.2f}".format(12.552)
output_c = "{:15.1f}".format(12.552)        #자동 반올림

print(output_a)
print(output_b)
print(output_c)
"""
"""
output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_a)
print(output_b)
print(type(output_a))
print(type(output_b))       #정수형이 아니라 문자열로 출력이 되는것
"""
"""
a = "HELLO"

print(a.lower())
"""
"""a = """

"""

print(a.strip())

"""

"""print("안녕" in "안녕하세요")"""

"""print("3+4 = {}".format(3+4))"""
"""
a= 2000

print(f"내가 지금 가진 돈이 {a}원 정도일껄")
"""
"""
print(False and False)
"""
"""if True:
    print("this True")
    print("real True!!")

"""
"""num = input("정수 입력 > ")
num = int(num)

if num > 0:
    print("양수")

if num == 0:
    print("0")

if num < 0:
    print("음수")
"""
"""
import datetime         #import -> 수입하다, 가져오다

now = datetime.datetime.now()

print(
    {}년 {}월 {}일 {}시 {}분 {}초.format(
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second
    )
)

"""

"""import datetime

now = datetime.datetime.now()



if now.hour < 12:
    print("now time{}, am".format(now.hour))

if now.hour >= 12:
    print("now time{}, pm".format(now.hour))"""

"""------------------------------2023.11.02-----------------------------------"""
"""# 주석
print("안냥","안녕")
print()
print("Hello"+"Bye")
print()
print("Bye"*3)
"""

"""print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])
print()
print("Hello"[-1])
print("Hello"[-2])
print("Hello"[-3])
print("Hello"[-4])
print("Hello"[-5])"""
"""
print("Hello"[2:4])
print()
# 파이썬은 맨 마지막 숫자를 포함하지 않는다
# 첫번째 숫자는 포함한다
print("감자탕먹을래?"[0:2]) #감자 0 1
print("감자탕먹을래?"[0:3]) #감자탕 0 1 2
print("감자탕먹을래"[3:])   #먹을래
print("감자탕먹을래"[:2])   #감자
# [] 은 인덱싱
# [:] 은 슬라이싱
"""
"""# len 은 문자열의 길이
print(len("Hello")) # 5
# type() 괄호안에 입력한 자료의 유형
print(type(10))     #int

pi = 3.14       # 파이썬은 변수에 자료형을 지정하지 않아도 된다.
print(type(pi)) # float
"""
"""# input -> 사용자 입력 함수
# 프롬프트에서 사용자가 입력하는것을 기다린다.
str = input("인사말을 입력해주세요> ")
print(str+"!!")     # Bye!!
print(type(str))    # str

num = input("숫자> ")   # 숫자를 입력해도
print(num)
print(type(num))    # str로 나오는것을 확인할 수 있음"""
"""
# 문자열을 숫자로 변환하는 것을 캐스트(cast)라고 한다.
#int() -> 문자열을 int 자료형으로 변환한다.
#float() -> 문자열을 float 자료형으로 변환한다.

string_a = input("input1 > ")
int_a = int(string_a)
string_b = input("input2 > ")
float_a = float(string_b)

print(type(int_a), int_a)      #int
print(type(float_a), float_a)    #float

# str() -> 다른 자료형을 문자형으로 변환한다.
test_a = str(int_a)
print(type(test_a), test_a)     #str
"""
"""
# format() -> {}기호를 format의 괄호 안에 있는 매개변수로 대체한다.
format_a = "{}won".format(5)
format_b = "{} {} {}".format(1, "문자열", True)

print(format_a)     # 5
print(format_b)     # 1 문자열 Ture

format_c = "{:5d}".format(52)   # 5칸 뒤로
print(format_c)     

#의미 없는 소수점 0 삭제 -> {:g}
float_a = 52.2500
format_d = "{:g}".format(float_a)   #00삭제
print(format_d)     # 52.25

# strip() -> 양옆 공백 제거 rstrip()/lstrip()
i = """
"""
print(i)            # 공백 있음
print(i.strip())    # 공백 없음

# find() / rfind() -> 문자열 찾기
i_a = "안녕안녕안녕안녕하세요".find("안녕")
print(i_a)
i_b = "안녕안녕안녕안녕하세요".rfind("안녕")
print(i_b)

# in 연산자 -> 문자열 내부에 확인하고싶은 문자열이 존재 하는지 여부를 묻는다.
print("Hello" in "Hello baby")

#split() -> 문자열 자르기 함수
a = "10 20 30 40 50".split(" ") # 띄어쓰기 기준으로 자르는것
print(a)    # 실행결과로 리스트가 나온다.

# f-문자열
fint_a = "{}".format(10)
fint_b = f'{10}'            #format 이렇게도 사용 가능
fint_c = f"{50} {30+5}"
print(fint_a,fint_b, fint_c)"""

"""# 구의 부피와 겉넓이
r = input("구의 반지름을 입력해주세요: ")
pi = 3.141592
r_cha = float(r)
val = pi*(r_cha*r_cha*r_cha)*(4/3)
knel = 4*pi*(r_cha*r_cha)
print("구의 부피는"+f"{val}"+"입니다.")
print("구의 겉넓이는"+f"{knel}"+"입니다.")

"""

"""# 피타고라스의 정리 빗변을 구하시오
a = float(input("밑변: "))
b = float(input("높이: "))

pro_c = (a*a)+(b*b)
c = pro_c **(0.5)
print("빗변 :"+f"{c}")
"""

"""
Hello
"""

print("Hello")