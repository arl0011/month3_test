import flet as ft
from database import Database

def main(page: ft.Page):
    page.title = "Список контактов"
    page.window.width = 600

    db = Database("contacts.db")
    db.create_tables()

    def get_rows():
        rows = []
        for contact in db.all_contacts():
            rows.append(
                ft.Row(
                    controls=[
                        ft.Text(str(contact[0]), width=30),
                        ft.Text(contact[1], expand=True),
                        ft.Text(contact[2], expand=True),
                        ft.Text(contact[3] or "", expand=True),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            icon_color=ft.colors.RED,
                            on_click=delete_contact,
                            data=contact[0],
                        ),
                    ]
                )
            )
        return rows

    def add_contact(e):
        name = name_input.value.strip()
        phone = phone_input.value.strip()
        note = note_input.value.strip()

        if not name or not phone:
            return

        db.add_contact(name, phone, note)
        contact_list.controls = get_rows()

        name_input.value = ""
        phone_input.value = ""
        note_input.value = ""

        page.update()

    def delete_contact(e):
        db.delete_contact(e.control.data)
        contact_list.controls = get_rows()
        page.update()

    title = ft.Text("Контакты", size=30)
    name_input = ft.TextField(label="Имя контакта", expand=True)
    phone_input = ft.TextField(label="Номер телефона", expand=True)
    note_input = ft.TextField(label="Дополнительная пометка", expand=True)
    add_button = ft.ElevatedButton("Добавить", on_click=add_contact)

    form = ft.Row(controls=[name_input, phone_input, note_input, add_button])

    contact_list = ft.Column(controls=get_rows(), scroll="auto", expand=True)

    page.add(title, form, contact_list)

ft.app(target=main)
