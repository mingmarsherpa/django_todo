# ToDo App
A simple and efficient ToDo application built with Django and MySQL.  
Manage your tasks, set deadlines, and keep track of your daily activities easily.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Add, update, and delete tasks
- Set deadlines for tasks
- select if the task is completed or pending
- View all tasks in a clean interface
- User authentication (signup and login)

## Installation
Follow these steps to run the project locally with **Pipenv** and **MySQL**:

```bash
# Clone the repository
git clone https://github.com/your-username/todo-app.git

# Navigate into the project folder
cd todo-app

# Install dependencies using Pipenv
pipenv install

# Activate the Pipenv shell
pipenv shell

# Make sure MySQL server is running and create a database
# Example:
# CREATE DATABASE todo_app_db;

# Update your Django settings.py DATABASES section with your MySQL credentials

# Apply migrations to set up the database
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
