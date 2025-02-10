# ToDoList
TODO List is a simple web application for managing daily tasks efficiently. Users can create, update, delete tasks, and mark them as completed.


# Project Setup Instructions

### 1. **Fork the Repository**

- Go to the repository on GitHub.
- Click the **Fork** button in the upper-right corner to create your own copy of the repository.

### 2. **Clone the Forked Repository**

- Copy the link to your fork by clicking the **Clone or download** button in your repository.
- Use the following command to clone the repository:

```git clone <link-from-your-forked-repo>```

- Replace <link-from-your-forked-repo> with the copied link.

### Create a Branch for Your Solution and Switch to It
Open the terminal in your IDE or project directory, and run the following command:

    git checkout -b develop

### Create a Virtual Environment
If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:

    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt

### Run tests:
    python manage.py test
