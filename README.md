
# EduTrack - Student Management System

EduTrack is a web-based Student Management System developed using Python and Django. It provides an interface for managing student records and academic courses through a centralized dashboard.

## Features

- Student registration and management
- Add, view, edit and delete student records
- Course creation and management
- Assign students to courses
- Search students by name or email
- Dashboard displaying student and course statistics
- User authentication and protected application pages
- SQLite database integration

## Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite
- **Version Control:** Git and GitHub

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/shreyankb04/EduTrack.git
cd EduTrack
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

### 7. Run the application

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Future Enhancements

- Attendance management
- Student performance tracking
- Advanced filtering and reporting
- Enhanced dashboard analytics

## Author

**Shreyank Borawake**
