# task_01_discount.py
# Программа рассчитывает цену со скидкой

price = float(input("Введите цену: "))
discount_percent = float(input("Введите скидку (%): "))

final_price = price * (1 - discount_percent / 100)
print(f"Цена со скидкой: {final_price:.2f} руб.")