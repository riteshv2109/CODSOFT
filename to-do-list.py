import json
import os
from datetime import datetime

class ToDoList:
    def __init__(self, filename='todo.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, description, due_date=None, priority='medium'):
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {description}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list!")
            return

        print("\nYour To-Do List:")
        print("-" * 50)
        for task in self.tasks:
            status = "✓" if task['completed'] else " "
            due_date = task['due_date'] if task['due_date'] else "No deadline"
            print(f"{task['id']}. [{status}] {task['description']}")
            print(f"   Priority: {task['priority'].title()}, Due: {due_date}")
            print(f"   Created: {task['created_at']}")
            print("-" * 50)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task {task_id} marked as completed!")
                return
        print(f"Task {task_id} not found!")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        print(f"Task {task_id} deleted!")

    def update_task(self, task_id, description=None, due_date=None, priority=None):
        for task in self.tasks:
            if task['id'] == task_id:
                if description:
                    task['description'] = description
                if due_date:
                    task['due_date'] = due_date
                if priority:
                    task['priority'] = priority
                self.save_tasks()
                print(f"Task {task_id} updated!")
                return
        print(f"Task {task_id} not found!")

def main():
    todo = ToDoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD, optional): ") or None
            priority = input("Enter priority (low/medium/high, default medium): ").lower() or 'medium'
            todo.add_task(description, due_date, priority)
        
        elif choice == '2':
            todo.list_tasks()
        
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as complete: "))
            todo.complete_task(task_id)
        
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            todo.delete_task(task_id)
        
        elif choice == '5':
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new description (leave blank to keep current): ") or None
            due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ") or None
            priority = input("Enter new priority (low/medium/high, leave blank to keep current): ").lower() or None
            todo.update_task(task_id, description, due_date, priority)
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()