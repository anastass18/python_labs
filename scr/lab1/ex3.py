price = float(input()) #вводим цену
discount = float(input()) #вводим скидку
vat = float(input()) #
base = price*(1-discount/100) #находим базу после скидки
vat_amount = base*(vat/100) #находим НДС
total = base + vat_amount #находим итог
print(f"База после скидки: {base:.2f} ₽") #выводим базу после скидки
print(f"НДС: {vat_amount:.2f} ₽") #выводим НДС
print(f"Итого: {total:.2f} ₽") #выводим итого