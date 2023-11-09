from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/registration')
def register():
   return render_template('registration.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/login_authentication', methods = ['POST'])
def login_auth():
    email = request.form.get('email')
    password = request.form.get('password')
    return "The email is {} and the password is {}.".format(email, password)

if __name__ == "__main__":
    app.run(debug = True)