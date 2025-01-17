import flet as ft

def main(page):
    title = ft.Text("Hashzap")
    
    def tunnel_send_message(message):
        text = ft.Text(message)
        chat.controls.append(text)
        page.update()

    page.pubsub.subscribe(tunnel_send_message)


    def send_message(event):
        name_user = box_name.value
        box_massage_text = box_send_message.value
        message = f"{name_user}: {box_massage_text}"
        page.pubsub.send_all(message)        

        text = ft.Text(box_send_message.value)
        chat.controls.append(text)
        page.update()

    box_send_message = ft.TextField(label="Write a message", on_submit=send_message)
    button_send = ft.ElevatedButton("Send", on_click=send_message)
    line = ft.Row([box_send_message, button_send])

    chat = ft.Column()

    def enter_chat(event):
        popup.open = False
        page.remove(title)
        page.remove(button)

        page.add(chat)
        page.add(line)

        name_user = box_name.value
        message = f"{name_user} entered the chat"
        page.pubsub.send_all(message)

        page.update()

    title_popup = ft.Text("Welcome to Hashzap")
    box_name = ft.TextField(label="Write your name")
    button_popup = ft.ElevatedButton("Enter in Chat", on_click=enter_chat)

    popup = ft.AlertDialog(
        title=title_popup,
        content=box_name,
        actions=[button_popup]
    )

    def open_popup(event):
        page.dialog = popup
        popup.open = True
        page.update()

    button = ft.ElevatedButton("Iniciar Chat", on_click=open_popup)
    page.add(title)
    page.add(button)

ft.app(main, view=ft.WEB_BROWSER)