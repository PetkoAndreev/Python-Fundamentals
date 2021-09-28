import json
import webbrowser
from tkinter.ttk import *
from tkinter import *
from tkinter.scrolledtext import *
from tkcalendar import DateEntry

tk = Tk()
tk.geometry('900x700')
tk.config(bg='skyblue')

all_tasks_to_write = []


def open_url():
    webbrowser.open_new('https://softuni.bg/')


def clear_view():
    for s in tk.grid_slaves():
        s.destroy()


def get_all_tasks_from_file():
    with open('db.txt', 'r') as file:
        try:
            existing_tasks = json.load(file)
        except json.decoder.JSONDecodeError:
            existing_tasks = []
    return existing_tasks


def write_tasks_to_file(all_tasks, existing_tasks=None):
    with open('db.txt', 'r+') as file:
        if not existing_tasks:
            existing_tasks = get_all_tasks_from_file()
        file.seek(0)
        file.truncate()
        all_tasks.extend(existing_tasks)
        json.dump(all_tasks_to_write, file)


def edit_task(task):
    existing_tasks = get_all_tasks_from_file()
    task_to_edit = existing_tasks[eval(task)]
    clear_view()
    Label(text="Enter your task name: ").grid(row=0, column=0, padx=20, pady=20)
    name = Entry(tk)
    name.delete(0, END)
    name.insert(0, task_to_edit['name'])
    name.grid(row=0, column=1, padx=20, pady=20)
    Label(tk, text="Due date: ").grid(row=1, column=0, padx=20, pady=20)
    date = DateEntry(tk)
    date.delete(0, END)
    date.insert(0, task_to_edit['due_date'])
    date.grid(row=1, column=1, padx=20, pady=20)
    Label(tk, text="Description: ").grid(row=2, column=0, padx=20, pady=20)
    description = ScrolledText(tk, width=20, height=10)
    description.insert(INSERT, task_to_edit['description'])
    description.insert(END, "")
    description.grid(row=2, column=1, padx=20, pady=20)
    Label(text=f"Select priority, current is {task_to_edit['priority'] if task_to_edit['priority'] != 0 else None}").grid(row=3, column=0, padx=20, pady=20)
    s = IntVar()
    rad1 = Radiobutton(tk, text='Low', value=1, variable=s)
    rad2 = Radiobutton(tk, text='Medium', value=2, variable=s)
    rad3 = Radiobutton(tk, text='High', value=3, variable=s)

    rad1.grid(column=1, row=3)
    rad2.grid(column=2, row=3)
    rad3.grid(column=3, row=3)
    Label(tk, text="Check if completed: ").grid(row=4, column=0, padx=20, pady=20)
    Label(tk, text="Check if completed: ").grid(row=4, column=0, padx=20, pady=20)
    chk_state = BooleanVar()
    chk_state.set(task_to_edit["is_completed"])  # set check state
    chk = Checkbutton(tk, text='Choose', var=chk_state)
    chk.grid(column=1, row=4)

    Button(tk, text="Edit task", bg="yellow", fg="black", command=lambda: write_tasks_to_file(all_tasks_to_write, task_to_edit)).grid(row=5, column=0)
    Button(tk, text="Cancel", bg="black", fg="white", command=lambda: render_main_view()).grid(row=5, column=1, padx=100, pady=100)


def delete_task(task):
    existing_tasks = get_all_tasks_from_file()
    existing_tasks.remove(eval(task))
    write_tasks_to_file(all_tasks_to_write, existing_tasks)


def render_list_task_view():
    clear_view()
    box = Combobox(width=100)
    existing_tasks = get_all_tasks_from_file()
    box['values'] = existing_tasks
    box.grid(row=0, column=0)
    Button(tk, text='Edit', bg='yellow', command=lambda: edit_task(box.get())).grid(row=1, column=0, pady=20)
    Button(tk, text='Delete', bg='red', command=lambda: delete_task(box.get())).grid(row=1, column=1, padx=30, pady=20)


def create_task(**kwargs):
    all_tasks_to_write.append(kwargs)


def render_create_task_view():
    clear_view()
    Label(text='Enter your task name: ').grid(row=0, column=0, padx=20, pady=20)
    task_name = Entry()
    task_name.grid(row=0, column=1)
    Label(text='Due date: ').grid(row=1, column=0, padx=20, pady=20)
    due_date = DateEntry()
    due_date.grid(row=1, column=1)
    Label(text='Description: ').grid(row=2, column=0, padx=20, pady=20)
    description = ScrolledText(width=20, height=10)
    description.grid(row=2, column=1, padx=20, pady=20)
    Label(text='Select priority: ').grid(row=3, column=0, padx=20, pady=20)
    selected_priority_num = IntVar()
    Radiobutton(text='Low', value=1, variable=selected_priority_num).grid(row=3, column=1, padx=20, pady=20)
    Radiobutton(text='Medium', value=2, variable=selected_priority_num).grid(row=3, column=2, padx=20, pady=20)
    Radiobutton(text='High', value=3, variable=selected_priority_num).grid(row=3, column=3, padx=20, pady=20)
    Label(text='Is completed? ').grid(row=4, column=0, padx=20, pady=20)
    is_completed = BooleanVar()
    Checkbutton(text='Check', variable=is_completed).grid(row=4, column=1, padx=20, pady=20)
    Button(tk, text='Create task', bg='green', fg='white', command=lambda: create_task(name=task_name.get(), due_date=due_date.get(), description=description.get('1.0', END), priority=selected_priority_num.get(), is_completed=is_completed.get())).grid(row=5, column=0, padx=20, pady=80)


def render_main_view():
    Button(tk, text='List tasks', bg='blue', fg='white', command=lambda: render_list_task_view()).grid(row=0, column=0, padx=200, pady=200)
    Button(tk, text='Create new task', bg='green', fg='white', command=lambda: render_create_task_view()).grid(row=0, column=1, padx=100, pady=200)
    Button(tk, text='Open URL', command=lambda: open_url()).grid(row=0, column=3)


render_main_view()
tk.mainloop()

write_tasks_to_file(all_tasks_to_write)