# Calendar Linda

A modern, clean calendar web application built with Python (Flask) and HTML/CSS. It features user authentication, a visual calendar, and event management.

## Features

*   User registration and login
*   Modern split layout design
*   Interactive calendar (middle section)
*   Event creation and display (right section)
*   Responsive design for desktop and mobile

## Screenshots

| Login/Register | Dashboard        |
| :------------- | :--------------- |
| (Add image)    | (Add image)      |

*Note: Add actual screenshots of your login/register and dashboard pages in the `docs/` folder if available.*

## Project Structure

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

## How to Run

1.  Clone or download this repository.
2.  Navigate to the project directory.
3.  Run the Flask app:

    ```
    python app.py
    ```
4.  Open your browser and go to `http://127.0.0.1:5000/`.

## Usage

*   **Register**: Create a new user account.
*   **Login**: Access your dashboard using your credentials.
*   **Dashboard**:
    *   View the current month's calendar in the middle section.
    *   Add events on the right.
*   **Logout**: Click the "Logout" button to end your session.

## Contributing

Feel free to fork this project, make changes, and submit pull requests.

## License

This project is open source and available under the [License Name] License.
