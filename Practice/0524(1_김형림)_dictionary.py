print('dictionary 1.\n')

students = [
   {"name" : "홍길동", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
   {"name" : "이몽룡", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
   {"name" : "성춘향", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
   {"name" : "변학도", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
   {"name" : "박지성", "korean" : 95, "math" : 98, "english" : 98, "science" : 98},
   {"name" : "류현진", "korean" : 64, "math" : 88, "english" : 92, "science" : 92}
]

print('이름\t\t총점\t\t평균')
for i in students :
   total = 0
   for a, b in i.items() :
      if a == "name" :
         name = b
      else :
         total += b
   print(f'{name}\t{total}\t\t{total/4}')

print('\n=======================\n')

print('dictionary 2.')

dictionary = {}

while True :
   word = input('\n영어 단어 등록 (종료는 quit) : ')
   if word == 'quit' :
      break
   while word in dictionary :
      print('%s(은)는 이미 등록된 단어입니다.' % word)
      word = input('\n영어 단어 등록 (종료는 quit) : ')
   meaning = input('%s의 뜻 입력 (종료는 quit) : ' % word)
   if meaning == 'quit' :
      break
   dictionary[word] = meaning

while True :
   search = input('\n검색할 단어 입력 (종료는 quit): ')
   if search == 'quit' :
      break
   while search not in dictionary :
      print('%s(은)는 사전에 없는 단어입니다.' % search)
      search = input('\n검색할 단어 입력 (종료는 quit) : ')
   result = dictionary[search]
   print('%s의 뜻은 %s입니다.' % (search, result))
   
print('\n종료합니다.')
print(dictionary)