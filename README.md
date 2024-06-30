# Project Management Tool

A collaborative project management tool built with Django.

## Installation

1. **Extract the Zip File**: Extract the contents of the zip file to a directory on your local machine.

2. **Create and Activate a Virtual Environment**:

    **Windows:**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    **macOS/Linux:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Collect Static Files**:

    ```bash
    python manage.py collectstatic
    ```

7. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```

8. **Access the Application**:

    Open a web browser and go to `http://127.0.0.1:8000/`.

## Usage

- Navigate to the Projects page to view and create projects.[Only superusers can create projects and tasks however admin can create special groups of users with different layers of restrictions]
- Assign tasks to team members and track progress.
- Use the admin interface at `http://127.0.0.1:8000/admin/` for advanced management.


## Screenshots

