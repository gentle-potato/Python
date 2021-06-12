# 리스트의 요소를 제거 : remove(), pop()

# remove(삭제하려는 값) : 가장 첫 번째 만나는 값을 삭제
n = [1, 2, 3, 4, 5, 3, 4, -1 ,-5, 10]
# n.remove(-1)
print(n)
cnt = n.count(3)
print(cnt)

# pop() : 맨 마지막 값을 삭제, 반환 / pop(index) : index 위치의 값을 삭제, 반환
data = n.pop(4)
print(n)
print(data)