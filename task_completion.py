# task_completion.py
import tkinter as tk
from tkinter import ttk, messagebox

class TaskComplete:
    def __init__(self, root, tasks):
        self.root = root
        self.tasks = tasks
        self.create_widgets()

    def create_widgets(self):
        # Task List Treeview
        self.task_list_treeview = ttk.Treeview(self.root, columns=("Task Name", "Priority", "Due Date"), show="headings")
        self.task_list_treeview.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        self.task_list_treeview.heading("Task Name", text="Task Name")
        self.task_list_treeview.heading("Priority", text="Priority")
        self.task_list_treeview.heading("Due Date", text="Due Date")

        # Populate Task List
        self.populate_task_list()

        # Mark Complete Button
        mark_complete_button = tk.Button(self.root, text="Mark Complete", command=self.mark_complete)
        mark_complete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    def populate_task_list(self):
        for task in self.tasks:
            self.task_list_treeview.insert("", tk.END, values=(task.name, task.priority, task.due_date))

    def mark_complete(self):
        selected_item = self.task_list_treeview.selection()
        if selected_item:
            task_name = self.task_list_treeview.item(selected_item)["values"][0]
            for task in self.tasks:
                if task.name == task_name:
                    confirmed = messagebox.askyesno("Confirm", f"Mark '{task_name}' as complete?")
                    if confirmed:
                        task.complete = True
                        self.task_list_treeview.delete(selected_item)
                    break

# Create a mock Task class for demonstration
class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.complete = False

# Mock tasks list
tasks = [
    Task("Task 1", "High", "2024-02-20"),
   
]

# Create a mock root window for testing
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskComplete(root, tasks)
    root.mainloop()
