from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/, ['GET', 'POST'])
@app.route('/', methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST': 
        # Retrieve the text from the textarea 
        text = request.form.get('textarea') 
  
        # Print the text in terminal for verification 
        print(text) 
  
    return render_template('home.html') 
  
@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
