# 재귀호출

# 팩토리얼 계산 함수 factorial()
# n! = n*(n-1)*(n-2)*...*2*1
def factorial1() :
    n = int(input('숫자 입력 : '))
    result = n
    for i in range(n-1, 0, -1) :
        result *= i
    return result

print(factorial1())

# 또는
#재귀함수 활용
def factorial2(n) :
    if n == 1:
        return 1
    return n * factorial2(n-1)   # 재귀함수

print(factorial2(5))
# f(4) : 4 * f(3) = 4 * 3 * 2 * 1
# f(3) : 3 * f(2) = 3 * 2 * 1
# f(2) : 2 * f(1) = 2 * 1
# f(1) : 1