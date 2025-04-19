# Calendar Linda

A modern, clean calendar web application inspired by Linda, built with Python (Flask) and HTML/CSS.

## Features (So Far)

- User registration and login with session management
- Clean, horizontally split UI for login, registration, and dashboard
- Responsive design for desktop and mobile
- Simple interactive calendar (month view) on the dashboard
- Logout functionality

## Screenshots

| Login/Register | Dashboard (Calendar) |
|---|---|
| ![Login Screenshot](docs/login.png) | ![Dashboard Screenshot](docs/dashboard.png) |

*(Add screenshots in the `docs/` folder if you wish!)*

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


---

### Running the App

1. Clone or download this repository.
2. Navigate to the project directory.
3. Start the Flask app:

    ```
    python app.py
    ```

4. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## Usage

- **Register:** Create a new account on the Register page.
- **Login:** Use your credentials to log in.
- **Dashboard:** View the current month’s calendar. (More features coming soon!)
- **Logout:** Click the logout link to end your session.

---

## Next Steps / Future Improvements

- Add event creation, editing, and deletion
- Store user and event data in a database (e.g., SQLite)
- Password hashing for improved security
- Enhanced calendar features (day/week view, reminders)
- Improved accessibility and animations

---

## License

This project is open source and free to use.

---

*Made with Flask & ❤️*


## Contact

For questions or suggestions, please open an issue or contact the project maintainer.

