print('=====1.=====')

print('<예측>')
print("[(0, 'apple'), (1, 'banana'), (2, 'grape')]")

print('<결과>')
mylist = ['apple' ,'banana', 'grape']
result = list(enumerate(mylist))
print(result)



print('\n\n=====2.=====')

print('<예측>')
print("{'my': 5, 'cat': 6, 'has': 2, 'blue': 3, 'eyes,': 4, 'is': 7, 'cute': 8}")

print('<결과>')
cat_song = "my cat has blue eyes, my cat is cute"
print({i:j for j,i in enumerate(cat_song.split())})





print('\n\n=====3.=====')

print('<예측>')
print('orage&pink&brown&black&&white')

print('<결과>')
colors = ['orange', 'pink', 'brown', 'black', 'white']
result = '&'.join(colors)
print(result)





print('\n\n=====4.=====')

print('<예측>')
print("{'students': 0, 'superuser': 1, 'professor': 2, 'employee': 3}")

print('<결과>')
user_dict = {}
user_list = ["students","superuser", "professor", "employee"]
for value_1, value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
print(user_dict)




print('\n\n=====5.=====')

print('[0, 2, 4, 6, 8]')
print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print("['zero', 'one', 'two', 'three']")
print('cs50')




print('\n\n====6.=====')
print('<예측>')
print("['Cat', 'Panda', 'Owl']")

print('<결과>')
animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl']
print([ani for ani in animal if 'o' not in ani])




print('\n\n====7.=====')
print('<예측>')
print('DongUniversity')

print('<결과>')
name = "Hanbit University"
student = ["Hong", "Gil", "Dong"]
split_name = name.split()
join_student = ''.join(student)
print(join_student[-4:] + split_name[1])




print('\n\n====8.=====')
print('<예측>')
print('20')

print('<결과>')
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score[0][2])




print('\n\n====9.=====')
print('[[12, 3], [15, 3]]')




print('\n\n====10.=====')
print('<예측>')
print('yellow')

print('<결과>')
week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
list_data = [week, rainbow]
print(list_data[1][2])




print('\n\n====11.=====')
print('<예측>')
print("score: 72")

print('<결과>')
kor_score = [30, 79, 20, 100, 80]
math_score = [43, 59, 0, 30, 90]
eng_score = [49, 72, 48, 67, 15]
midterm_score = [kor_score, math_score, eng_score]
print ("score:",midterm_score[2][1])




print('\n\n====12.=====')
print('<예측>')
print("['a', '2', 'error']")

print('<결과>')
alist = ["a", "b", "c"]
blist = ["1", "2", "3"]
abcd= []
for a, b in enumerate(zip(alist, blist)):
    try:
        abcd.append(b[a])
    except IndexError:
        abcd.append("error")
print(abcd)




print('\n\n====13.=====')
print('zip')

print('<결과>')
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2' ,'b3']

for a, b in zip(alist, blist):
    print(a, b)




print('\n\n====14.=====')
print('<예측>')
print('80')

print('<결과>')
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0]
print(len(answer))