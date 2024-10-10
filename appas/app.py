
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('test.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    address = request.form['address']
    
    
    return f"Hello, {name}! Your form was submitted successfully.<br>This is your info: Your age is {age}, your email is {email}, and your address is: {address}."

if __name__ == '__main__':
    app.run(debug=True)



