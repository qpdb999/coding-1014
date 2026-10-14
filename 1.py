# Python 변수와 자료형 (Variables, Data Types)
'''

    오늘 배운 내용

1. 변수(Variable)

변수는 데이터를 저장하고 사용하기 위해 이름을 붙인 공간이다.

  기본 형식

python
변수명 = 값


  사용 예시

python
name = "철수"
age = 16
height = 170.5

print(name)
print(age)
print(height)


  출력 결과

text
철수
16
170.5


- 변수는 = 기호를 사용해 값을 저장한다.
- 파이썬은 변수에 값을 저장할 때 자료형을 직접 작성하지 않아도 된다.
- 변수에 새로운 값을 저장하면 기존 값이 변경된다.

  변수 값 변경하기

python
score = 70
print(score)

score = 90
print(score)


  출력 결과

text
70
90


2. 자료형(Data Type)

자료형은 데이터가 어떤 종류의 값인지 나타낸다.

파이썬에서 자주 사용하는 기본 자료형은 다음과 같다.

| 자료형 | 설명 | 예시 |
|     |     |       |
| int | 정수 | 10, -5 |
| float | 실수 | 3.14, 170.5 |
| str | 문자열 | "Hello" |
| bool | 참 또는 거짓 | True, False |

  사용 예시

python
age = 16
height = 170.5
name = "철수"
is_student = True

print(age)
print(height)
print(name)
print(is_student)


  출력 결과

text
16
170.5
철수
True


3. type()

type()`은 변수에 저장된 값의 자료형을 확인할 때 사용하는 함수이다.

  기본 형식

python
type(값)


  사용 예시

python
age = 16
height = 170.5
name = "철수"
is_student = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))


  출력 결과

text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>


- type()을 사용하면 값이 정수인지, 실수인지, 문자열인지 확인할 수 있다.
- 자료형을 확인하면 데이터에 맞는 연산이나 처리를 선택하는 데 도움이 된다.

4. 자료형 변환

자료형 변환은 데이터를 다른 자료형으로 바꾸는 것이다.

| 함수 | 기능 | 예시 |
|         |             |                   |
| int() | 정수로 변환 | int("10") → 10 |
| float() | 실수로 변환 | float("3.5") → 3.5 |
| str() | 문자열로 변환 | str(10) → "10" |
| bool() | 참 또는 거짓으로 변환 | bool(1) → True |

  사용 예시

python
num1 = "10"
num2 = "20"

result = int(num1) + int(num2)

print(result)
print(type(result))


  출력 결과

text
30
<class 'int'>


문자열인 "10"과 "20"을 int()로 정수로 변환한 뒤 더했다.

 int()는 "3.5"처럼 소수점이 포함된 문자열을 바로 정수로 변환할 수 없다. 이 경우에는 float("3.5")를 사용해야 한다.

5. 변수와 자료형 활용하기

사용자에게 이름과 나이를 입력받아 정보를 출력하는 프로그램이다.

python
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
height = float(input("키를 입력하세요: "))

print("이름:", name)
print("나이:", age)
print("키:", height)
print("이름의 자료형:", type(name))
print("나이의 자료형:", type(age))
print("키의 자료형:", type(height))


  실행 결과 예시

text
이름을 입력하세요: 철수
나이를 입력하세요: 16
키를 입력하세요: 170.5
이름: 철수
나이: 16
키: 170.5
이름의 자료형: <class 'str'>
나이의 자료형: <class 'int'>
키의 자료형: <class 'float'>

     복습하면서 알게 된 점

- 변수는 데이터를 저장하고 사용하기 위한 이름이다.
- 파이썬에서는 = 기호로 변수에 값을 저장한다.
- int, float, str, bool은 자주 사용하는 기본 자료형이다.
- type()은 값의 자료형을 확인할 때 사용한다.
- int(), float(), str() 등을 이용하면 자료형을 변환할 수 있다.
- input()은 기본적으로 문자열을 반환하므로 숫자 계산을 할 때는 적절한 자료형으로 변환해야 한다.


📌 AI 활용 복습 문제

  1. 변수의 역할은 무엇인가?

1. 프로그램을 종료한다.  
2. 데이터를 저장하고 사용한다.  
3. 화면을 꾸민다.  
4. 반복문을 실행한다.

    정답 2

  2. 다음 중 정수 자료형은 무엇인가?

1. 3.14 
2. "100"  
3. 100 
4. True

    정답 3

  3. 다음 중 실수 자료형은 무엇인가?

1. 10
2. 2.5
3. "Hello" 
4. False

    정답 2

  4. 문자열 자료형을 나타내는 것은 무엇인가?

1. int 
2. float
3. bool 
4. str

    정답 4

  5. 다음 코드의 출력 결과는 무엇인가?

python
score = 70
score = 90
print(score)


1. 70  
2. 90  
3. 160  
4. 오류 발생

    정답 2

  6. 변수의 자료형을 확인하는 함수는 무엇인가?

1. input()
2. type()
3. print() 
4. int()
    
    정답 2

  7. 다음 코드의 출력 결과는 무엇인가?

python
num = int("10")
print(num + 5)


1. 105
2. 10 + 5
3. 15
4. 오류 발생

    정답 3

  8. 다음 중 올바른 설명은 무엇인가?

1. input()은 기본적으로 정수를 반환한다.  
2. float()는 문자열을 항상 정수로 변환한다.  
3.파이썬에서는 변수에 값을 저장할 때 자료형을 직접 선언하지 않아도 된다.  
4. type()은 변수에 새로운 값을 저장한다.

    정답 3
'''