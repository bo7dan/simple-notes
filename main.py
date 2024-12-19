import datetime



class Note:
    def __init__(self, title, text, category):
        self.title = title
        self.text = text
        self.category = category
        self.creation_date = datetime.datetime.now()

    def __str__(self):
        return f"Заголовок: {self.title}\nКатегорія: {self.category}\nДата створення: {self.creation_date}\nТекст:\n{self.text}\n"



class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, text, category):
        new_note = Note(title, text, category)
        self.notes.append(new_note)

    def view_notes(self):
        if not self.notes:
            print("Немає нотаток.")
        else:
            for note in self.notes:
                print(note)
                print("-" * 40)

    def edit_note(self, title, new_text):
        for note in self.notes:
            if note.title == title:
                note.text = new_text
                print("Нотатку відредаговано.")
                return
        print("Нотатку з таким заголовком не знайдено.")

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print("Нотатку видалено.")
                return
        print("Нотатку з таким заголовком не знайдено.")



def display_menu():
    print("1. Додати нову нотатку")
    print("2. Переглянути всі нотатки")
    print("3. Редагувати нотатку")
    print("4. Видалити нотатку")
    print("5. Вихід")



def main():
    notebook = Notebook()

    while True:
        display_menu()
        choice = input("Оберіть опцію: ")

        if choice == "1":
            title = input("Введіть заголовок нотатки: ")
            text = input("Введіть текст нотатки: ")
            category = input("Введіть категорію нотатки: ")
            notebook.add_note(title, text, category)
            print("Нотатку додано.\n")

        elif choice == "2":
            notebook.view_notes()

        elif choice == "3":
            title = input("Введіть заголовок нотатки для редагування: ")
            new_text = input("Введіть новий текст нотатки: ")
            notebook.edit_note(title, new_text)

        elif choice == "4":
            title = input("Введіть заголовок нотатки для видалення: ")
            notebook.delete_note(title)

        elif choice == "5":
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.\n")


if __name__ == "__main__":
    main()
