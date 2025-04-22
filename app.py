from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory user store (for demonstration only)
users = {}
# Add this near the top, after users = {}
events = {}  # {username: { 'YYYY-MM-DD': [event1, event2, ...], ... }, ... }

from datetime import datetime

@app.route('/add_event', methods=['POST'])
def add_event():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    date = request.form['date']
    event = request.form['event']
    if username not in events:
        events[username] = {}
    if date not in events[username]:
        events[username][date] = []
    events[username][date].append(event)
    flash('Event added!')
    return redirect(url_for('home'))

@app.route('/get_events')
def get_events():
    if 'username' not in session:
        return {}
    username = session['username']
    user_events = events.get(username, {})
    return user_events

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists')
        else:
            users[username] = password
            flash('Registration successful! Please log in.')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
