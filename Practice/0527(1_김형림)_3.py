print('====== 3. 회원명단 작성 ======')

# input_member(input_file명)
def input_member(input_file) :
    with open(input_file, 'w', encoding='utf-8') as f :
        x = input('멤버를 입력하세요. (종료는 q) : ')
        while True :
            if x != 'q' :
                f.write(x + '\n')
                x = input('멤버를 입력하세요. (종료는 q) : ')
            else :
                print('저장되었습니다!')
                break

# output_member(output_file명)
def output_member(output_file) :
    with open(output_file, 'r', encoding='utf-8') as g :
        while True :
            line = g.readline()
            if line == '' :
                break
            print(line, end='')

# main()
def main() :
    while True :
        do = input('저장 1, 출력 2, 종료 q : ')
        if do not in ('1', '2', 'q') :
            print('1, 2, q 중에서 하나만 입력하세요!')
        elif do == '1' :
            input_file = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
            input_member(input_file)
        elif do == '2' :
            output_file = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
            output_member(output_file)
        elif do == 'q' :
            break

if __name__ == '__main__' :
    main()