print('====== 2. 두 개의 숫자 더하기 ======')

def sum(x, y) :
    # 숫자가 저장된 파일을 불러와서 공백을 기준으로 분할
    # 저장할 파일 또한 불러옴
    f = open(x, 'r', encoding='utf-8')
    g = open(y, 'a', encoding='utf-8')
    data = f.read()
    data = data.split()
    data = list(map(int, data))
    # print(data)

    # 두 수의 합을 리스트로 만들어서, 최종적으로 세로로 출력
    results = []
    for i in range(len(data)) :
        if i % 2 == 0 :
         results.append(data[i] + data[i+1])
        else :
            results.append(0)

    for i in range(len(results)) :
        if i % 2 == 0 :
            if data[i+1] < 0 :
                g.write(f'{data[i]}-{abs(data[i+1])}={results[i]:.1f}\n')
            else :
                g.write(f'{data[i]}+{data[i+1]}={results[i]:.1f}\n')
    f.close()
    g.close()

if __name__ == '__main__' :
    sum('sum.txt', 'save.txt')