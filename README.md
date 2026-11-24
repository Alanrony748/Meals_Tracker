# Meals_Tracker

A Django REST Framework-based Meals Tracker API that allows users to manage their food diary, track daily calorie intake, and monitor body weight.

## Project Overview

Meals Tracker is a REST API developed using Django REST Framework. It provides functionality for user registration, food diary management, calorie tracking, and weight monitoring. It also includes JWT-based authentication with login, token refresh, and logout functionality.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Simple JWT
- REST API

## Features

### User Management
- User registration
- User authentication
- JWT access and refresh token generation
- Token refresh
- Logout using refresh token blacklisting

### Food Diary
- Add food entries
- View food diary records
- Update food entries
- Delete food entries
- Store food name, meal type, quantity, calories, date, and notes
- Associate food records with users

### Weight Tracker
- Record body weight
- View weight records
- Store recording date and notes
- Associate weight records with users

## Project Structure

```text
meals_tracker/
│
├── Food_Diary/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── meals_tracker/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/signup/` | Register a new user |
| POST | `/login/` | Login and generate JWT tokens |
| POST | `/refresh/` | Refresh access token |
| POST | `/logout/` | Logout and blacklist refresh token |
| GET | `/user/` | Retrieve user information |
| GET | `/food/` | Retrieve food entries |
| POST | `/food/` | Add a food entry |
| PUT | `/food/<id>/` | Update a food entry |
| DELETE | `/food/<id>/` | Delete a food entry |
| GET | `/weight/` | Retrieve weight records |
| POST | `/weight/` | Add a weight record |

*Note: Update the refresh endpoint path in this table if your final URL configuration uses `/token/refresh/` instead of `/refresh/`.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Alanrony748/Meals_Tracker.git
```

### 2. Navigate to the project directory

```bash
cd Meals_Tracker
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

## JWT Authentication

The project uses Simple JWT for authentication.

1. Register a user through the signup endpoint.
2. Login using username and password.
3. Receive access and refresh tokens.
4. Use the access token in the Authorization header:

```text
Authorization: Bearer <access_token>
```

5. Use the refresh token to obtain a new access token.
6. Logout by submitting the refresh token to the logout endpoint.

## Testing

API endpoints can be tested using Postman or a VS Code REST Client HTTP file.

## Author

**Alan Rony**

GitHub: [Alanrony748](https://github.com/Alanrony748)

---

Developed as a Django REST Framework project to practice backend development, REST API design, database management, and JWT authentication.