# main Example
name = ''

def inputName() :
    global name
    name = input('이름 입력 : ')
    # return name   # global을 사용하면 return이 필요 없어짐!

def getName() :
    if name == '' :
        return '무명씨'
    else :
        return name

def main() :
    inputName()
    print(getName())

if __name__ == '__main__' :
    main()