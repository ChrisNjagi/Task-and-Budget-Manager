#list to store data




class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False
        
        
    def mark_completed(self):
        self.completed = True 
        
tasks = []
expenses = []

#function to display menu

def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Add Expense")
    print("4. View Expenses")
    print("5. Exit")
    
    
    #function to add task
def add_task():
    title = input("Enter task title: ")
    priority = input("Enter task priority (High/Medium/Low): ")
    
    new_task = Task(title, priority)
    tasks.append(new_task)    
    print("Task added successfully!")
    
#function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    

    
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1].mark_completed()
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")
    
    print("\n---Your Tasks---")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task.completed else "Pending"
        print(f"{index}. {task.title} | Priority: {task.priority} | Status: {status}")
        
        #function to add expense
def add_expense():
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    
    category = input("Enter expense category: ")
    
    expense = {
        "name": name,
        "amount": amount,
        "category": category
        
    }
    expenses.append(expense)
    print("Expense added successfully!")
    
    #function to view expenses
def view_expenses():
    if not expenses:
        print("No expenses found.")
        return
    
    total = 0
    print("\n---Your Expenses---")
    
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} | Amount: ${expense['amount']} | Category: {expense['category']}")
        total += expense['amount']
        
    print(f"\nTotal Expenses: ${total}")
    
    #main loop
    
while True:
    show_menu()
    choice = input("Enter your option: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        add_expense()
    elif choice == "4":
        view_expenses()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    
        
    else:
        print("Invalid choice. Please try again.")
        
        
        # funtion to mark task as completed
def mark_task_completed():
    if not tasks:
        print("No tasks found.")
        return
    
    view_tasks()
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1].mark_completed()
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")