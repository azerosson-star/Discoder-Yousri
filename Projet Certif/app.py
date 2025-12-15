"""
FLASK AUTHENTICATION APPLICATION
=================================
A simple user authentication system with registration, login, and logout functionality.

Features:
- User registration with password hashing
- User login with session management
- Protected routes (users must be logged in)
- Password security using werkzeug

Why Flask? Lightweight web framework perfect for small to medium applications.
Why Werkzeug? Provides cryptographic password hashing for security.
Why Sessions? Keeps users logged in across multiple page visits.
"""

# IMPORT REQUIRED LIBRARIES
# =========================
from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Fonction utilitaire pour obtenir une connexion
def get_db_connection():
    conn = sqlite3.connect('BDD.db')  # ton fichier SQLite
    conn.row_factory = sqlite3.Row   # pour pouvoir accéder aux colonnes par nom
    return conn


# INITIALIZE FLASK APPLICATION
# =============================
# Create a Flask app instance - this is the core of our web application
# It handles routing, template rendering, and request management
app = Flask(__name__)

# SET SECRET KEY FOR SESSION ENCRYPTION
# ======================================
# The secret key is used to encrypt session data stored in user cookies
# If attacker doesn't know this key, they can't forge sessions or steal data
# IMPORTANT: In production, use a strong random key, not a hardcoded one!
# BETTER: Load from environment variable: os.getenv('SECRET_KEY')
app.secret_key = "un_truc_long_et_secret"

# IN-MEMORY USER DATABASE
# =======================
# Dictionary to store users: { "username": "hashed_password" }
# This simulates a database. In production, use SQLite, PostgreSQL, etc.
# Why a dict? Fast lookups by username, easy to understand for learning
# Why in-memory? Data is lost when server restarts (fine for demo)
#
# Example after 2 registrations:
# users_db = {
#     "alice": "pbkdf2:sha256:260000$...",
#     "bob": "pbkdf2:sha256:260000$..."
# }
users_db = {}

# ROUTE 1: CONNECTION PAGE
# ========================
# Display the login/registration page
# This route serves the HTML form to the user
@app.route("/connexion")
def connexion():
    """
    Render the connection/login page.
    URL: http://localhost:5000/connexion
    Methods: GET (only)
    Returns: HTML template 'connexion.html'
    
    Why separate route? Allows users to access the login form.
    Why separate template? Keeps HTML organized, not mixed with Python.
    """
    return render_template("connexion.html")

# ROUTE 2: HOME PAGE
# ==================
# Show different content based on login status
@app.route('/')
def accueil():
    """
    Home page with conditional content based on login status.
    URL: http://localhost:5000/
    Methods: GET (only)
    
    Flow:
    1. Check if 'username' exists in session dictionary
    2. If yes: user is logged in -> show welcome message + logout link
    3. If no: user is not logged in -> show welcome message + login/register links
    
    Sessions:
    - Session is a dictionary stored in encrypted user cookie
    - Survives browser refresh/page navigation
    - Expires when browser closes (or after timeout)
    
    Returns: HTML string with content appropriate for user status
    """
    if 'username' in session:
        # User is logged in
        # session['username'] contains their username
        return f"Hello, {session['username']}! <a href='/logout'>Logout</a>"
    
    # User is not logged in
    return "Welcome! <a href='/login'>Login</a> or <a href='/register'>Register</a>"

# ROUTE 3: USER REGISTRATION
# ===========================
# Handle both displaying registration form and processing registration
@app.route('/register', methods=['POST'])
def register():
    """
    Handle user registration (sign up).
    URL: http://localhost:5000/register
    Methods: POST (form submission)
    
    Process:
    1. Get username and password from form submission
    2. Check if username already exists
    3. If exists: reject, show error, let user try again
    4. If new: hash password, store in database, redirect to login
    
    Why hash passwords?
    - If database is breached, attackers get hashes, not actual passwords
    - Hashes are one-way: can't convert hash back to password
    - Even with same password, different hashes are generated (salt)
    - When user logs in, we hash their input and compare with stored hash
    
    Why redirect to login?
    - Forces user to verify they can log in with their credentials
    - Creates explicit login session (not automatic after registration)
    
    Flow chart:
    POST /register
        ↓
    Get username + password from form
        ↓
    Username exists in users_db?
        ├→ YES: Return error message
        └→ NO: Hash password → Store in DB → Redirect to /login
    """
    if request.method == 'POST':
        # Extract form data
        username = request.form['nom']   # Get username from form
        password = request.form['password']   # Get password from form
        
        # CHECK IF USERNAME ALREADY EXISTS
        # Prevent duplicate accounts with same username
        if username in users_db:
            return "Username already exists. <a href='/register'>Try again</a>."
        
        # HASH THE PASSWORD
        # generate_password_hash() uses PBKDF2 with SHA256
        # Applies salt (random data) to prevent rainbow table attacks
        # Creates irreversible hash of password
        hashed_password = generate_password_hash(password)
        
        # STORE NEW USER IN DATABASE
        # Key: username, Value: hashed password
        users_db[username] = hashed_password
        
        # REDIRECT TO LOGIN PAGE
        # User must now log in with their new credentials
        return redirect('/login')
    
    # If not POST request, show registration form HTML
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Register">
        </form>
    '''

# ROUTE 4: USER LOGIN
# ===================
# Handle both displaying login form and processing login
@app.route('/login', methods=['POST'])
def login():
    """
    Handle user login.
    URL: http://localhost:5000/login
    Methods: POST (form submission)
    
    Process:
    1. Get username and password from form submission
    2. Look up username in database
    3. If found: compare provided password with stored hash
    4. If match: create session, redirect to home
    5. If not match: show error, let user try again
    
    Why compare hashes instead of passwords?
    - We never store plain passwords
    - We hash the user input and compare with stored hash
    - If hashes match, we know password is correct
    
    Sessions:
    - session['username'] = username stores data in encrypted cookie
    - This cookie is sent with every request to server
    - Server decrypts it using secret_key to access data
    - Persists across page navigation
    
    Flow chart:
    POST /login
        ↓
    Get username + password from form
        ↓
    Username exists in users_db?
        ├→ NO: Return error
        └→ YES: Hash input password, compare with stored hash
            ├→ MISMATCH: Return error
            └→ MATCH: Create session → Redirect to /
    """
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']   # Get username from form
        password = request.form['password']   # Get password from form
        
        # LOOK UP USER IN DATABASE
        # Get the stored hashed password for this username
        # .get() returns None if username doesn't exist (safe)
        hashed_password = users_db.get(username)
        
        # VALIDATE CREDENTIALS
        # Two conditions must be true:
        # 1. User exists (hashed_password is not None)
        # 2. Password matches (check_password_hash compares input with stored hash)
        if hashed_password and check_password_hash(hashed_password, password):
            # PASSWORD IS CORRECT
            # Create session for this user
            session['username'] = username
            
            # Redirect to home page
            # Now home() will see 'username' in session and show logged-in content
            return redirect('/')
        
        # PASSWORD IS INCORRECT OR USER DOESN'T EXIST
        return "Invalid credentials. <a href='/login'>Try again</a>."
    
    # If not POST request, show login form HTML
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# ROUTE 5: LOGOUT
# ===============
# Clear the user session and return to home
@app.route('/logout')
def logout():   
    """
    Handle user logout.
    URL: http://localhost:5000/logout
    Methods: GET (link click)
    
    Process:
    1. Remove username from session dictionary
    2. Redirect to home page
    3. Home page will now show logged-out content
    
    session.pop() explanation:
    - Removes 'username' key from session dictionary
    - Second argument 'None' is default if key doesn't exist (no error)
    - After this, session is empty
    
    Flow:
    GET /logout
        ↓
    session.pop('username', None)  [Remove user session]
        ↓
    Redirect to /  [Go to home page]
        ↓
    home() runs, 'username' not in session
        ↓
    Display logged-out content
    """
    # Remove the username from the session dictionary
    session.pop('username', None)
    
    # Redirect to lgin page
    return redirect('accueil.html')