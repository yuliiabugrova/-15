from tkinter import*
from tkinter.filedialog import*
from tkinter.messagebox import*
from tkinter.colorchooser import askcolor

def new_file():
    text_area.delete(1.0, END)

def open_file():
    file = askopenfile(mode="r")
    if file is not None:
        contetn = file.read()
        text_area.delete(1.0, END)
        text_area.insert(END, contetn)
        file.close()

def save_file():
    file = asksaveasfile(mode="w", defaultextension=".text")
    if file is not None:
        data = text_area.get(1.0, END)
        file.write(data)
        file.close()

def exit_app():
    if askyesno("Закрити", "Закрити програму?"):
        root.destroy()

def change_text_color():
    color = askcolor(color=text_area["fg"]) [1]
    if color:
        text_area.configure(fg=color)

def change_background_color():
    color = askcolor(color=text_area["bg"]) [1]
    if color:
        text_area.configure(bg=color)

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Past>>")

def show_about():
    showinfo("Про програму", "Блокнот v1.0\nАвтор: Бугрова Юлія 1-СОМ")

def show_help():
    showinfo("Довідка", "Документація про діалогові вікна:\nhttps://docs.python.org/uk/3/library/dialog.html")

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

root=Tk()
root.title("Блокнот")

#Головне меню
menu_bar = Menu(root)
root.config(menu=menu_bar)

#Текстова область
text_area = Text(root, undo=True)
text_area.pack(fill=BOTH, expand=True)

#Меню файл
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Новий", command=new_file)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Вийти")

#Меню редагування
edit_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Редарування", menu=edit_menu)
edit_menu.add_command(label="Вирізати", command=cut_text)
edit_menu.add_command(label="Копіювати", command=copy_text)
edit_menu.add_command(label="Вставити", command=paste_text)

#Меню формат
format_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Формат", menu=format_menu)
format_menu.add_command(label="Колір тексту", command=change_text_color)
format_menu.add_command(label="Колір фону", command=change_background_color)

#Меню Довідка 
help_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Довідка", menu=help_menu)
help_menu.add_command(label="Про програму", command=show_about)
help_menu.add_command(label="Довідка про діалогові вікна", command=show_help)

#Контекстне меню
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Колір тексту", command=change_text_color)
context_menu.add_command(label="Колір фону", command=change_background_color)
context_menu.add_command(label="Зберегти", command=save_file)
text_area.bind("<Button-3>", show_context_menu)
root.mainloop()