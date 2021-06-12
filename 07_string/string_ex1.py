# email type을 체크

email = input('input email : ')
if(email.find('@') == -1 or   # @가 없으면 X
        email.find('.') == -1 or   # .이 없으면 X
        email.index('@') > email.index('.') or   # .이 @보다 앞에 있으면 X
        email.index('.') - email.index('@') < 2 or   # .과 @가 붙어있으면 X
        email.index('@') == 0 or   # @가 맨 앞에 있으면 X
        len(email) - email.index('.') <= 1 or   # .이 맨 뒤에 있으면 X
        email.count('@') >= 2 or   # @가 2개 이상이면 X
        email.count('.') >= 2) :   # .이 2개 이상이면 X
    print('이메일 형식이 아닙니다.')
print('입력한 이메일 : %s' % email)