
total_price = int(input())
total_type_cnt = int(input())
def checkReceipt(total_price, product_type_cnt):
    varification_total_price = 0    # 확인용 변수
    for n in range(product_type_cnt):
        price_and_cnt = list(map(int, input().split(" ")))
        varification_total_price += price_and_cnt[0] * price_and_cnt[1]
    if varification_total_price == total_price: print("Yes") 
    else: print("No")
    return 
    

checkReceipt(total_price, total_type_cnt)
