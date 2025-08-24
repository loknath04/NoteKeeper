# Notes Keeper 📝

Notes Keeper is a simple web application built with Flask that allows users to register, log in, and securely manage their personal notes. The application provides a clean and intuitive interface for creating, editing, and deleting notes.

## Features ✨

- **User Authentication:** Secure user registration, login, and logout functionality.
- **Personal Dashboard:** A private dashboard to view all your notes.
- **Note Management:** Easily add, edit, and delete notes.
- **Secure Data Storage:** Notes and user data are stored in a local SQLite database.
- **Responsive Design:** A modern, professional user interface that works on various screen sizes.

## Technologies Used 🛠️

**Backend:**
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF

**Database:**
- SQLite

**Frontend:**
- HTML5
- CSS3

## Installation and Setup 🚀

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Python 3.x installed on your system.
- A code editor (e.g., VS Code).

### Steps

1. **Clone the repository:**
    ```bash
    git clone <your_repository_url_here>
    cd notes-keeper
    ```
    > Replace `<your_repository_url_here>` with the actual URL if available.

2. **Create a virtual environment:**  
    It's recommended to use a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the dependencies:**  
    The project uses a few Python libraries. Install them using pip.
    ```bash
    pip install Flask Flask-SQLAlchemy Flask-Login Flask-WTF
    ```

5. **Run the application:**
    ```bash
    python app.py
    ```
    The application will start, and you will see a message in your terminal indicating the local server address, typically [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage Guide 📋

- **Register:** Navigate to the `/register` page to create a new user account.
- **Login:** Use your new credentials to log in on the `/login` page.
- **Dashboard:** After logging in, you will be redirected to your personal dashboard, where you can see all your notes.
- **Add a Note:** Click the "+ Add Note" button to create a new note with a title and content.
- **Edit/Delete:** Each note card on the dashboard has buttons to edit or delete the note.

