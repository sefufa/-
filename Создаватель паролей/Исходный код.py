import random
import string
import tkinter as tk
from tkinter import messagebox
import os

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:  
            messagebox.showwarning("Ошибка", "Длина пароля должна быть не менее 4 символов.")
            return
        
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        result_var.set(password)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число для длины пароля.")

def copy_to_clipboard():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  
        messagebox.showinfo("Скопировано", "Пароль скопирован в буфер обмена.")
    else:
        messagebox.showwarning("Ошибка", "Сначала сгенерируйте пароль.")

def save_to_file():
    password = result_var.get()
    if not password:
        messagebox.showwarning("Ошибка", "Сначала сгенерируйте пароль.")
        return
    
    try:
        file_name = entry_filename.get()
        if not file_name:
            messagebox.showwarning("Ошибка", "Введите имя файла.")
            return
        
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        
        with open(file_name, "w") as file:
            file.write(f"Ваш сгенерированный пароль: {password}\n")
        
        messagebox.showinfo("Сохранено", f"Пароль сохранен в файл: {file_name}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")   
root = tk.Tk()
root.title("Генератор паролей")
root.geometry("400x400")  

tk.Label(root, text="Длина пароля:", font=("Arial", 12)).pack(pady=10)
entry_length = tk.Entry(root, font=("Arial", 12))
entry_length.pack()

tk.Button(root, text="Сгенерировать пароль", font=("Arial", 12), command=generate_password).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font=("Arial", 12), state="readonly", width=30).pack(pady=10)

tk.Button(root, text="Копировать в буфер", font=("Arial", 12), command=copy_to_clipboard).pack(pady=10)

tk.Label(root, text="Имя файла для сохранения:", font=("Arial", 12)).pack(pady=10)
entry_filename = tk.Entry(root, font=("Arial", 12))
entry_filename.pack()

tk.Button(root, text="Сохранить в файл", font=("Arial", 12), command=save_to_file).pack(pady=10)

root.mainloop()
