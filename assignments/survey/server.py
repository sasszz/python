from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Any string you wish, but KEEP DO NOT SHARE IT'

# Renders index.html at http://localhost:5000/html
@app.route('/')
def landing_page():
    return render_template('index.html')

# Gathers user's input at http://localhost:5000/users, stores in session and redirects to http://localhost:5000/show
# NOTE: Always Redirect on a POST, never render
@app.route('/users', methods=['POST'])
def create_user():
    print('Got Post Info')
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    return redirect('/show')

# Display user's Post submission
@app.route('/show')
def show_user():
    return render_template('show.html')

if __name__=='__main__':
    app.run(debug=True)