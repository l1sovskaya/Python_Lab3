def print_all_values(baggage_dict):
    """Виведення на екран усіх значень словника."""
    if not baggage_dict:
        print("\nСловник порожній.")
        return
    print("\nДані про багаж пасажирів:")
    for baggage_id, data in baggage_dict.items():
        print(f"Номер багажу: {baggage_id} | Кількість речей: {data[0]} шт. | Вага: {data[1]} кг")

def add_record(baggage_dict):
    """Додавання нового запису до словника з обробкою винятків."""
    print("\n--- Додавання нового багажу ---")
    try:
        baggage_id = int(input("Введіть унікальний номер багажу (ціле число): "))
        if baggage_id in baggage_dict:
            print("Помилка: Багаж з таким номером вже існує!")
            return
        
        items_count = int(input("Введіть кількість речей: "))
        weight = float(input("Введіть загальну вагу багажу (кг): "))
        
        if items_count < 0 or weight < 0:
            print("Помилка: Кількість речей та вага не можуть бути від'ємними.")
            return

        baggage_dict[baggage_id] = (items_count, weight)
        print(f"Запис успішно додано!")
    except ValueError:
        print("Помилка вводу: Очікувалося числове значення.")

def remove_record(baggage_dict):
    """Видалення запису зі словника за ключем із обробкою KeyError."""
    print("\n--- Видалення багажу ---")
    try:
        baggage_id = int(input("Введіть номер багажу для видалення: "))
        # спроба видалити за ключем
        del baggage_dict[baggage_id]
        print(f"Багаж номер {baggage_id} успішно видалено.")
    except ValueError:
        print("Помилка вводу: Номер багажу має бути цілим числом.")
    except KeyError:
        print(f"Помилка: Багаж з номером {baggage_id} не знайдено (неіснуючий ключ).")

def print_sorted_by_keys(baggage_dict):
    """Перегляд вмісту словника за відсортованими ключами."""
    if not baggage_dict:
        print("\nСловник порожній.")
        return
    print("\nДані про багаж (відсортовані за номером):")
    # функція sorted для ключів
    for baggage_id in sorted(baggage_dict.keys()):
        data = baggage_dict[baggage_id]
        print(f"Номер багажу: {baggage_id} | Кількість речей: {data[0]} шт. | Вага: {data[1]} кг")

def solve_variant_task(baggage_dict):
    """Розв'язання завдання варіанту 20."""
    if not baggage_dict:
        print("\nНеможливо виконати завдання: словник порожній.")
        return
    
    print("\n--- Результати виконання завдання варіанту 20 ---")
    
    # а) кількість пасажирів, які мають більше двох речей
    count_more_than_two = sum(1 for data in baggage_dict.values() if data[0] > 2)
    print(f"а) Кількість пасажирів з більше ніж 2 речами: {count_more_than_two}")
    
    # б) чи є хоч один пасажир, багаж якого складається з 1 речі вагою менше 25 кг
    has_light_item = any(data[0] == 1 and data[1] < 25 for data in baggage_dict.values())
    if has_light_item:
        print("б) Чи є пасажир з 1 річчю вагою < 25 кг: ТАК")
    else:
        print("б) Чи є пасажир з 1 річчю вагою < 25 кг: НІ")
        
    # в) номер багажу, в якому вага 1 речі відрізняється від загальної середньої не більше ніж на 0,5 кг
    total_items = sum(data[0] for data in baggage_dict.values())
    total_weight = sum(data[1] for data in baggage_dict.values())
    
    if total_items > 0:
        global_avg_weight = total_weight / total_items
        print(f"   (Довідково: загальна середня вага однієї речі = {global_avg_weight:.2f} кг)")
        
        matching_ids = []
        for b_id, data in baggage_dict.items():
            if data[0] > 0:
                local_avg_weight = data[1] / data[0]
                if abs(local_avg_weight - global_avg_weight) <= 0.5:
                    matching_ids.append(b_id)
        
        if matching_ids:
            print(f"в) Номери багажу, що відповідають умові: {', '.join(map(str, matching_ids))}")
        else:
            print("в) Багажу, що відповідає умові, не знайдено.")
    else:
        print("в) Неможливо обчислити, оскільки загальна кількість речей дорівнює нулю.")

def main():
    # початковий словник. ключ: номер багажу. значення: кортеж (кількість_речей, загальна_вага)
    # задано n = 10 згідно з варіантом.
    baggage_data = {
        101: (3, 45.0),
        102: (1, 20.0),
        103: (2, 30.5),
        104: (4, 60.0),
        105: (1, 26.0),
        106: (2, 28.0),
        107: (5, 75.0),
        108: (1, 15.0),
        109: (3, 46.5),
        110: (2, 31.0)
    }

    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1. Вивести всі записи словника")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Переглянути словник (відсортовано за ключами)")
        print("5. Виконати індивідуальне завдання (Варіант 20)")
        print("0. Вийти з програми")
        
        choice = input("Оберіть дію (0-5): ")
        
        if choice == '1':
            print_all_values(baggage_data)
        elif choice == '2':
            add_record(baggage_data)
        elif choice == '3':
            remove_record(baggage_data)
        elif choice == '4':
            print_sorted_by_keys(baggage_data)
        elif choice == '5':
            solve_variant_task(baggage_data)
        elif choice == '0':
            print("Роботу завершено.")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
