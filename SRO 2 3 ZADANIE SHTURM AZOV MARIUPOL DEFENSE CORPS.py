def bank_simulation():
    queue = []
    while True:
        print("\n--- Меню банка ---")
        print("1. Добавить клиента в очередь")
        print("2. Обслужить следующего клиента")
        print("3. Показать текущую очередь")
        print("4. Выйти")
        
        choice = input("Выберите действие (1-4): ")
        if choice == '1':
            name = input("Введите имя клиента: ")
            queue.append(name)
            print(f"Клиент {name} встал в очередь.")
        
        elif choice == '2':
            if len(queue) > 0:
                served_client = queue.pop(0)
                print(f"Клиент {served_client} обслужен и покинул банк.")
            else:
                print("Очередь пуста!")
        
        elif choice == '3':
            if not queue:
                print("В очереди никого нет.")
            else:
                print("Текущая очередь:", " <- ".join(queue))
        
        elif choice == '4':
            print("Работа завершена.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")
if __name__ == "__main__":
    bank_simulation()
