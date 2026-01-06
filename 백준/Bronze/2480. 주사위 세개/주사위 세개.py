
input = list(map(int,input().split(" ")))

def prize_money(dices):
    # count 함수를 사용하기
    # dice 숫자가 dices 리스트 내에 몇 개가 있는지 확인
    # 만약 2개 또는 3개라면 break
    # 만약 1개라면 continue
    duplication_dice = ""    

    for dice in dices:
        count = dices.count(dice)
        if count == 2:
            return print(1000 + (dice * 100))
        elif count == 3:
            return print(10000 + (dice * 1000))
    
    # for 문을 통과하는 값은 무조건 모든 주사위가 서로 다른 수일 경우임

    max_dice = max(dices)

    return print(max_dice * 100)

prize_money(input)