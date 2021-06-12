# 주문액, 할인액, 지불액 연습문제(딕셔너리 활용)
print('# 주문액, 할인액, 지불액 연습문제')

def order(p, q) :
    total = p * q
    if total >= 100000 :
        discount = 0.1
    elif total >= 50000 :
        discount = 0.05
    else :
        discount = 0
    after_discount = total * (1 - discount)
    # 딕셔너리 값으로 반환
    info = {'가격': p,
            '수량': q,
            '주문액': total,
            '할인율': discount,
            '할인액': total * discount,
            '지불액': after_discount}
    return info

p = int(input('상품 가격 입력 : '))
q = int(input('주문 수량 입력 : '))
print('--------------------')
order = order(p, q)
for key in order.keys() :
    print(f'{key:} : {order[key]:>10,.0f}')