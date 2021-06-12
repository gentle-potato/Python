# replce()
text = 'Java Programming'
text = text.replace('Java', 'Python')
print(text)

# 대문자/소문자 변환
# upper(), lower(), capitalize(), title(), swapcase()
text = 'java programming is Fun'
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

# 공백문자 제거 strip(), lstrip(), rstrip()
text = '     java programming is Fun     '
print(text + '---')
print(text.strip())
print(text.lstrip())
print(text.rstrip() + '---')