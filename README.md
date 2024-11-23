# Task Manager

## Overview

Task Manager is a Python program designed to help users efficiently manage their tasks. The program allows adding, removing, and updating tasks, as well as viewing priority tasks, overdue tasks, and marking tasks as completed.

## Features

- Add tasks with a name, due date, priority, and status.
- Remove tasks by their name.
- View all tasks in a clear and structured format.
- Highlight priority tasks for quick identification.
- Display overdue tasks based on the current date.
- Mark tasks as "Done" when completed.
- Save tasks persistently in a CSV file.

## How It Works

1. The program reads tasks from a CSV file (`task.csv`) at startup.
2. Users interact with the program via a menu-driven interface:
   - **Option 1:** Add a new task.
   - **Option 2:** Remove an existing task.
   - **Option 3:** View all tasks.
   - **Option 4:** View priority tasks.
   - **Option 5:** View overdue tasks.
   - **Option 6:** Mark a task as completed.
3. Tasks are saved to the CSV file when the program exits.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AI-Tonny/Task-Manager.git
