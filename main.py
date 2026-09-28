#обновленый епта
tasks = []


def show_tasks():
    if not tasks:
        print("Список задач пуст.")
    else:
        print("\nСписок задач:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


while True:
    print("\n===== СПИСОК ЗАДАЧ =====")
    print("1. Добавить задачу")
    print("2. Показать список задач")
    print("3. Удалить задачу")
    print("4. Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        task = input("Введите задачу: ")
        tasks.append(task)
        print("Задача добавлена.")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()

        if tasks:
            try:
                number = int(input("Введите номер задачи для удаления: "))

                if 1 <= number <= len(tasks):
                    deleted_task = tasks.pop(number - 1)
                    print(f"Задача «{deleted_task}» удалена.")
                else:
                    print("Такого номера нет.")

            except ValueError:
                print("Введите число.")

    elif choice == "4":
        print("Программа завершена.")
        break

    else:
        print("Неверный пункт меню.")