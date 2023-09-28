time1 = int(input("Введите время: "))
price1 = int(input("Сумма купленого товара."))
if time1<9:
    print("Акция действует с 10 до 12")
elif time1>13:
    print("Акция уже закончилась")
else:
    print('К оплате', (price1)/2)