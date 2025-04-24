from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Define User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(200))
    events = db.relationship('Event', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database if it doesn't exist
with app.app_context():
    if not os.path.exists('instance/calendar.db'):
        db.create_all()

# Routes
@app.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('home.html', username=current_user.username)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
            
        login_user(user)
        return redirect(url_for('home'))
        
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user:
            flash('Username already exists')
            return redirect(url_for('register'))
            
        new_user = User(username=username)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/add_event', methods=['POST'])
@login_required
def add_event():
    date = request.form['date']
    event_description = request.form['event']
    
    new_event = Event(
        date=date,
        description=event_description,
        user_id=current_user.id
    )
    
    db.session.add(new_event)
    db.session.commit()
    
    flash('Event added!')
    return redirect(url_for('home'))

@app.route('/get_events')
@login_required
def get_events():
    events_query = Event.query.filter_by(user_id=current_user.id).all()
    
    # Convert to format expected by the frontend
    events_by_date = {}
    for event in events_query:
        if event.date not in events_by_date:
            events_by_date[event.date] = []
        events_by_date[event.date].append({"id": event.id, "description": event.description})
    
    return jsonify(events_by_date)

@app.route('/delete_event/<int:event_id>', methods=['POST'])
@login_required
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    
    # Check if the event belongs to the current user
    if event.user_id != current_user.id:
        flash('You do not have permission to delete this event')
        return redirect(url_for('home'))
    
    db.session.delete(event)
    db.session.commit()
    
    flash('Event deleted')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
