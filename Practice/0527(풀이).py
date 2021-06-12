# ===== 1. =====

### 허영대 작성 ###
with open('yesterday.txt', 'r', encoding='utf-8') as f :
    textFile = f.readlines()
    wordCounter = dict()
    for line in textFile :
        if line.endswith("\n") :
            line = line[:-1]
        wordList = line.lower().split(' ')
        for word in wordList :
            if word in wordCounter :
                wordCounter[word] += 1
            else:
                wordCounter[word] = 1

print(wordCounter)

### 김정명 작성 ###
with open('yesterday.txt', 'r', encoding='utf-8') as f :
    # 딕셔너리로 저장해서 출력
    dic = dict()

    # 모든 파일을 불러와서 공백 기준으로 쪼개기
    # lines에 있는 모든요소를 소문자
    lines = list(f.read().split())
    lines = list(map(lambda x: x.lower(), lines))

    # key값을 나타내기 위해 set으로 중복제거 후 리스트변환
    # 그 리스트를 오름차순 정렬
    temp_lines = list(set(lines))
    temp_lines.sort()

    # key값을 하나씩 불러와서 lines리스트 중 단어를 count한 값을 저장
    for line in temp_lines :
        dic[line] = lines.count(line)

# dic을 item으로 불러와 차례대로 출력
print("[출력결과 : 단어별 빈도]")
for k, v in dic.items() :
    print(f"'{k}': {v}")

# ===== 2. =====

### 채길호 작성 ###
def sum(input,result):
    with open(result,'w',encoding='utf-8') as result:
        with open(input,'r',encoding='utf-8') as f:
            data = f.read().split().copy()
            for i in range(len(data)):
                if i%2==0:
                    if int(data[i+1])<0:
                        sic = data[i] + data[i+1]
                        sum_result = str(int(data[i])+int(data[i+1]))
                        result.write(sic)
                        result.write('=')
                        result.write(sum_result + '\n')
                    else:
                        sic = data[i] + '+' + data[i+1]
                        sum_result = str(int(data[i])+int(data[i+1]))
                        result.write(sic)
                        result.write('=')
                        result.write(sum_result + '\n')

if __name__ == '__main__':
    sum('sum.txt','save_채길호.txt')

# ### 강아름 작성 ###   # 줄마다 빈 칸 들어간 거 miss
# def sum(inputfile, outputfile):
#     temp = []
#
#     g = open(inputfile, 'r')
#     r = open(outputfile, 'w')
#
#     for i in g.readlines():
#         temp = i.split()
#         r.write('%s + %s = %.1f\n' % (temp[0], temp[1], float(temp[0]) + float(temp[1])))
#
#     g.close()
#     r.close()
#
#
# sum('sum.txt', 'save_강아름.txt')

# ===== 3. =====

### 조민호 작성 ###
def input_member(input_filename):
    while True:
        name = input('멤버를 입력하세요.(종료는 q) : ')
        if name == 'q':
            return
        with open(input_filename, 'a', encoding='utf-8') as f:
            f.write(name+'\n')

def output_member(output_filename):
    with open(output_filename, 'r', encoding='utf-8') as f:
        data = f.read()
    print(data)


def main():
    while True:
        order = input('저장 1, 출력 2, 종료 q : ')
        if order == '1':
            input_filename = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
            input_member(input_filename)
        elif order == '2':
            output_filename = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
            output_member(output_filename)
        elif order == 'q':
            break

main()

### 장우창 작성 ###
# 멤버 입력하는 함수
def input_member(inputfile):
    ifile = open(inputfile, 'w', encoding='utf8')
    while True :
        mem = input('멤버를 입력하세요. (종료는 q) : ')
        if mem == 'q' :
            break
        ifile.write(mem+'\n')
    ifile.close()
    print('저장되었습니다.')

# 멤버 출력하는 함수
def output_member(outputfile):
    ofile = open(outputfile, 'r', encoding='utf8')
    while True :
        line = ofile.readline()
        if line == '' :     # 마지막 줄이면 while문 끝내기
            break
        print(line, end='')
    ofile.close()

if __name__ == '__main__' :
    print('3번 문제. 회원 명단 입출력')
    while True :
        command = input('저장 1, 출력 2, 종료 q : ')
        if command == 'q' :
            break
        elif command == '1' :
            filename = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
            input_member(filename)
        elif command == '2' :
            filename = input('멤버 명단이 저장된 파일명을 입력하세요 : ')
            output_member(filename)