import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    
    #stocks the user owns
    user = session['user_id']
    
    for (int i = 0; i < symbol; i++)
    
        symbol = db.execute('SELECT symbol FROM buy WHERE username = ?', user)[0]['symbol']
        result = lookup(symbol)
        name = result['name']
        price = db.execute('SELECT price FROM buy WHERE username = ?', user)[0]['price']
        time = db.execute('SELECT time FROM buy')
        #number of shares owned
        shares = db.execute('SELECT shares FROM buy WHERE username = ?', user)[0]['shares']
        #current price of each stock
        current_price = result['price']
        #value of each holding share*price
        current_value = current_price * shares
        #current cash balance
    
    current_cash = db.execute("SELECT cash FROM users")
    #grand total
    
    headings = ('Symbol', 'Company Name', 'Price', 'Time', 'Shares', 'Current price')
    data = (
        (symbol, name, price, time, shares, current_price),
        
        )
        
    
    return render_template("index.html", data=data, headings=headings)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == 'GET':
        return render_template('buy.html')

    result = lookup(request.form.get('symbol'))
    if not result:
        return render_template('buy.html', invalid=True, symbol= symbol)
        
    username = session['user_id']   
    symbol = request.form.get('symbol')
    shares = int(request.form.get('shares'))
    result = lookup(symbol)
    price = result['price']
    name = result['name']
    
    cash = db.execute('SELECT cash FROM users WHERE id = ?', username)[0]['cash']
    bill = cash - shares*price
    
    if bill < 0:
        return apology('Not enough cash')
    
    now = datetime.now()
    
    db.execute('UPDATE users SET cash = ? WHERE id = ?', bill, username)
    db.execute('INSERT into buy (username, symbol, shares, price, time) VALUES (?, ?, ?, ?, ?)', username, symbol, shares, price, now)
    
    return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    
    if request.method == 'GET':
        return render_template('quote.html')
    symbol = request.form.get('symbol')
    result = lookup(symbol)
    if not result:
        return render_template('quote.html', invalid=True, symbol= symbol)
    return render_template('quoted.html', name = result['name'], price= usd(result['price']), symbol = result['symbol'])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    
    if request.method == 'GET':
        return render_template('register.html')
        
    username = request.form.get('username')
    password = request.form.get('password')
    confirmation = request.form.get('confirmation')
    
    if username == "" or len(db.execute('SELECT username FROM users WHERE username = ?', username)) > 0:
        return apology("Invalid Username: Blank, or already exists")
    if password == "" or password != confirmation:
        return apology("Invalid Password: Blank, or does not match")
    
    db.execute('INSERT INTO users (username, hash) VALUES (?, ?)', username, generate_password_hash(password))
    
    rows = db.execute('SELECT * FROM users WHERE username = ?', username)
    
    session['user_id'] = rows[0]['id']

    return redirect('/')
    
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
