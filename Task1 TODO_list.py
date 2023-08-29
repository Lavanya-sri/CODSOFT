import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def edit_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_index)
        entry_task.delete(0, tk.END)
        entry_task.insert(tk.END, task)
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def remove_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_task = tk.Label(frame, text="Task:")
label_task.grid(row=0, column=0, sticky="w")

entry_task = tk.Entry(frame, width=30)
entry_task.grid(row=0, column=1, padx=5, pady=5)

btn_add = tk.Button(frame, text="Add Task", width=20, command=add_task)
btn_add.grid(row=1, column=0, columnspan=2, pady=5)

btn_edit = tk.Button(frame, text="Edit Task", width=20, command=edit_task)
btn_edit.grid(row=2, column=0, columnspan=2, pady=5)

btn_remove = tk.Button(frame, text="Remove Task", width=20, command=remove_task)
btn_remove.grid(row=3, column=0, columnspan=2, pady=5)

btn_clear = tk.Button(frame, text="Clear All", width=20, command=clear_tasks)
btn_clear.grid(row=4, column=0, columnspan=2, pady=5)

listbox_tasks = tk.Listbox(frame, height=10, width=40)
listbox_tasks.grid(row=5, column=0, columnspan=2, pady=5)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.grid(row=5, column=2, sticky="ns")
listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

root.mainloop()
