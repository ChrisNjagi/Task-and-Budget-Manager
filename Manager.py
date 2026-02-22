#list to store data

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
    
    task = {
        "title": title,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    
#function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n---Your Tasks---")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} | Priority: {task['priority']} | Status: {status}")
        
        #function to add expense
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
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
        total += expense["amount"]
        
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