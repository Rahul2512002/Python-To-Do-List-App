import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root=root
        self.root.title("TO-Do List")
        self.tasks=[]
        self.frame=tk.Frame(root)
        self.frame.pack(pady=10)
        self.listbox=tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar=tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(sid=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.entry=tk.Entry(root, width=50)
        self.entry.pack(pady=5)
        self.add_button=tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        self.delete_button=tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)
        self.complete_button=tk.Button(root, text="Mark as Completed", command=self.complete_task)
        self.complete_button.pack(pady=5)

    def add_task(self):
        task=self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "YOu must enter a task.")

    def delete_task(self):
        try:
            selected_task_index=self.listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must enter a task to delete.")

    def complete_task(self):
        try:
            selected_task_index=self.listbox.curselection()[0]
            self.tasks[selected_task_index]=f"{self.tasks[selected_task_index]} (completed)"
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__=="__main__":
    root=tk.Tk()
    app=ToDoApp(root)
    root.mainloop()
















