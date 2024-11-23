from datetime import datetime
import csv


def Read_csv(csv_file):
    """
    Reads tasks from a CSV file into a list of dictionaries.

    Args:
        csv_file (str): The name of the CSV file to read from.

    Returns:
        list: A list of dictionaries where each dictionary represents a task.
    """
    database = []
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)

    return database


def Write_csv(database, csv_file):
    """
    Writes the current task list (database) to a CSV file.

    Args:
        database (list): A list of dictionaries where each dictionary represents a task.
        csv_file (str): The name of the CSV file to write to.
    """
    with open(csv_file, "w", newline="") as file:
        fieldnames = ["Task", "Data", "Status", "Priority"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(database)


def getDate(prompt):
    """
    Prompts the user for a date and validates it in 'dd-mm-yyyy' format.

    Args:
        prompt (str): The message shown to the user.

    Returns:
        str: The validated date string in 'dd-mm-yyyy' format.
    """
    date_str = input(prompt)
    try:
        valid_date = datetime.strptime(date_str, '%d-%m-%Y')
        return valid_date.strftime('%d-%m-%Y')
    except ValueError:
        print('Invalid date format. Please enter the date in dd-mm-yyyy format')
        return getDate(prompt)


def AddTask(database):
    """
    Adds a new task to the database with fields Task, Data, Status, and Priority.

    Args:
        database (list): The list of tasks to which the new task will be added.
    """
    task = input("Enter Task name: ")
    date = getDate("Enter the end date of the task (dd-mm-yyyy): ")
    priority = bool(input("The task is a priority (0-no, 1-yes): "))

    database.append({"Task": task, "Data": date, "Status": "Not Done", "Priority": priority})


def RemoveTask(database):
    """
    Removes a task from the database by its name.

    Args:
        database (list): The list of tasks from which the task will be removed.
    """
    task = input("Enter Task name: ")

    for dataTask in database:
        if task == dataTask["Task"]:
            database.remove(dataTask)
            print(f"Task {dataTask} removed")
            break
    else:
        print("Task not found, please try again.")


def PrintTask(database):
    """
    Prints all tasks in the database with their details.

    Args:
        database (list): The list of tasks to be printed.
    """
    print("Name\tData\tStatus\tPriority")
    for dataTask in database:
        print(f"{dataTask['Task']} - {dataTask['Data']} - {dataTask['Status']} - {dataTask['Priority']}")


def PrintPriorityTask(database):
    """
    Prints tasks marked as priority.

    Args:
        database (list): The list of tasks to check and print if marked as priority.
    """
    f = 0
    for dataTask in database:
        if str(dataTask["Priority"]) == "True":
            f = 1
            print(f"{dataTask['Task']} - {dataTask['Data']} - {dataTask['Status']} - {dataTask['Priority']}")

    if f == 0:
        print("Priority task not found.")


def PrintMissedTask(database):
    """
    Prints tasks that are past their due date and are not marked as 'Done'.

    Args:
        database (list): The list of tasks to check and print if overdue.
    """
    f = 0
    for dataTask in database:
        if dataTask["Data"] < datetime.now().strftime("%d-%m-%Y") and dataTask["Status"] != "Done":
            f = 1
            print(f"{dataTask['Task']} - {dataTask['Data']} - {dataTask['Status']} - {dataTask['Priority']}")

    if f == 0:
        print("Missed Task not found.")


def MarkTaskExecuted(database):
    """
    Marks a specific task as 'Done' by its name.

    Args:
        database (list): The list of tasks in which a specific task will be marked as done.
    """
    task = input("Enter Task name: ")
    for dataTask in database:
        if task == dataTask["Task"]:
            dataTask["Status"] = "Done"
            break
    else:
        print("Task not found, please try again.")

def main():
    """
    The main function that manages the program menu and user choices.
    """
    csv_file = "task.csv"
    database_task = Read_csv(csv_file)

    print("Menu.")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Print Task")
    print("4. Print Priority Task")
    print("5. Print Missed Task")
    print("6. Mark Task Executed")
    while (choice := input("Enter your choice (press q to quit): ").lower()) != "q":

        match choice:
            case "1":
                AddTask(database_task)
            case "2":
                RemoveTask(database_task)
            case "3":
                if len(database_task) != 0:
                    PrintTask(database_task)
                else:
                    print("Database empty.")
            case "4":
                if len(database_task) != 0:
                    PrintPriorityTask(database_task)
                else:
                    print("Database empty.")
            case "5":
                if len(database_task) != 0:
                    PrintMissedTask(database_task)
                else:
                    print("Database empty.")
            case "6":
                if len(database_task) != 0:
                    MarkTaskExecuted(database_task)
                else:
                    print("Database empty.")
            case _:
                print("Invalid choice, please try again.")

    Write_csv(database_task, csv_file)
    print("Exiting...")

if __name__ == '__main__':
    main()
