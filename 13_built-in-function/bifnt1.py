#
print(all([0, 1, 2, 3]))
print(any([0, 1, 0]))
print(any([0, '', 0]))
print(any([0, [], 0]))

# ascii code value : chr(x)
print(chr(65))   # A
print(chr(97))   # a

# ord(c) : 아스키 코드값 반환
print(ord('a'))
print(ord('\n'))
print(ord(' '))
print(ord('\t'))
print(ord('\\'))

# bin(), oct(), hex(), int(), float(), str()

# divmod(a, b) : 몫과 나머지를 튜플 형태로 반환
print(divmod(7, 3))

# eval(expression) : expression을 평가하여 반환
print(eval('13.5'))
print(type(eval('13.5')))
print(eval('3+5'))

# help() : 함수에 대한 설명
help(print)
help(map)
help(sum)