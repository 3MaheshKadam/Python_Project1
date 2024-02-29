# task.py

class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.complete = False

tasks = []  # List to store tasks
