# 등록된 ID : flower
# 비밀번호 : 1234

ID = 'flower'
PW = '1234'

input_id = input('아이디 입력 : ')
input_pw = input('비밀번호 입력 : ')

if(input_id==ID and input_pw==PW):
    print("로그인 성공")
else:
    print('로그인 실패')
