import hashlib
from flask import Flask, render_template, request, redirect, session, url_for, flash, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',  
        user='root',
        password='',
        database='carnival_kingdom',
        port=3306
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/rides')
def rides():
    return render_template('rides.html')

@app.route('/water')
def water():
    return render_template('water.html')

@app.route('/land')
def land():
    return render_template('land.html')

@app.route('/all')
def all():
    return render_template('all.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        try:
            # Hash the input password
            hashed_password = hash_password(password)
            
            # Check user credentials
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", 
                           (username, hashed_password))
            user = cursor.fetchone()
            
            if user:
                # Set session for logged-in user
                session['logged_in'] = True
                session['username'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password', 'danger')
        
        except Exception as e:
            print(f"Login error: {e}")
            flash('An error occurred during login', 'danger')
        
        finally:
            cursor.close()
            conn.close()
    
    return render_template('login.html')

@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            # Hash the password
            hashed_password = hash_password(password)
            
            # Insert new user
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                           (username, email, hashed_password))
            conn.commit()
            
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
        
        except mysql.connector.IntegrityError:
            flash('Username or email already exists', 'danger')
        except Exception as e:
            print(f"Signup error: {e}")
            flash('An error occurred during signup', 'danger')
        
        finally:
            cursor.close()
            conn.close()
    
    return render_template('sign.html')

@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if not session.get('logged_in'):
        flash('Please log in to access the dashboard', 'danger')
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        # Fetch user's bookings
        cursor.execute("SELECT * FROM bookings WHERE name = %s", (session['username'],))
        bookings = cursor.fetchall()
        
        return render_template('dashboard.html', bookings=bookings)
    
    except Exception as e:
        print(f"Dashboard error: {e}")
        flash('An error occurred while fetching dashboard data', 'danger')
    
    finally:
        cursor.close()
        conn.close()

@app.route('/ticket_booking', methods=['GET', 'POST'])
def ticket_booking():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from frontend
        name = data.get('name')
        email = data.get('email')
        tickets = data.get('tickets')
        visit_date = data.get('visit-date')
        ticket_type = data.get('ticket-type')

        print(f"Received booking request - Name: {name}, Email: {email}, Tickets: {tickets}, Visit Date: {visit_date}, Ticket Type: {ticket_type}")
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO bookings (name, email, tickets, visit_date, ticket_type) VALUES (%s, %s, %s, %s, %s)",
                           (name, email, tickets, visit_date, ticket_type))
            conn.commit()
            print("Booking inserted successfully into database.")
            flash('Ticket booked successfully!', 'success')
            return redirect(url_for('ticket_booking'))
        except Exception as e:
            print(f"Database error: {e}")
            flash('Error booking ticket: ' + str(e), 'danger')

    return render_template('ticket_booking.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO contact_us (name, email, message) VALUES (%s, %s, %s)",
                          (name, email, message))
            conn.commit()
            return render_template('contact_success.html')
        except Exception as e:
            print(f"Database error: {e}")
            return render_template('contact_success.html')
        finally:
            cursor.close()
            conn.close()
            
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)