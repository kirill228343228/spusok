fruits = ["Яблуко", "Банан", "Грушка", "Апельсин", "Вишня"]

print("Список фруктів:")
for fruit in enumerate(fruits, start=1):
    print(fruit)

while True:
    try:
        a = int(input("Введіть номер фрукта (1-5): "))

        if a < 1 or a > len(fruits):
            print("Будь ласка, введіть номер між 1 і 5", len(fruits))
        else:
            print(f"Ви обрали: {fruits[a - 1]}")
            break

    except ValueError:
        print("Будь ласка, введіть ціле число.")