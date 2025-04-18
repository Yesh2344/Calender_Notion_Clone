# Calendar Linda

A simple calendar web application inspired by Linda, built with Python (Flask) and HTML.  
This initial version includes user registration and login functionality.

---

## Features (Implemented So Far)

- User registration with username and password
- User login and logout
- Simple dashboard page after login

---

## Project Structure


calendar_linda/
│
├── app.py # Main Flask application
├── templates/ # HTML templates
│ ├── login.html # Login page template
│ ├── register.html # Registration page template
│ └── home.html # Dashboard page template
└── static/
└── style.css # Basic CSS styling


---

## Prerequisites

- Python 3.x installed on your system
- Flask Python package

Install Flask via pip if you haven't already:

```
pip install flask
```
---

## How to Run

1. Clone or download this repository.
2. Navigate to the project folder in your terminal.
3. Run the Flask application:

```
python app.py
```

4. Open your web browser and go to:

```
https://127.0.0.1:5000/
```

---

## Usage

- **Register:** Create a new user account.
- **Login:** Access your dashboard using your credentials.
- **Dashboard:** See a welcome message (calendar features coming soon).
- **Logout:** End your session.

---

## Future Improvements

- Add interactive calendar view with event management
- Store user data in a database instead of in-memory dictionary
- Implement password hashing for security
- Add user profile and settings pages
- Responsive and improved UI design

