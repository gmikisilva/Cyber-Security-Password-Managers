from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Go to /login.squarespace.com to see the login page."

@app.route('/login.squarespace.com/api/1/login/oauth/provider/authorize')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
