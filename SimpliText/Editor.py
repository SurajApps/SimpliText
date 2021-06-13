from guizero import App, TextBox, MenuBar


def text_editor():
    file_name = ""
    window_width = 580
    window_height = 350

    def new_file():
        print("New File")

    def open_file():
        print("Open File")

    def save_file():
        print("Save File")

    def quit_app():
        print("Quit")

    app = App(title=file_name, width=window_width, height=window_height, layout="grid")
    menu_bar = MenuBar(app, toplevel=["File"], options=[[["New", new_file], ["Open", open_file], ["Save", save_file], ["Quit", quit_app]]])

    text_box = TextBox(app, multiline=True, scrollbar=True, width="fill", height="fill", grid=[0, 0], visible=True, enabled=True)

    app.display()


text_editor()
