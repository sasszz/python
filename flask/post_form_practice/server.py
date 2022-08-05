from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Any string you want"

@app.route('/users', methods=['POST']) # needs methods to specify POST route
def create_user():
    # print("Got Post Info")
    print(request.form['key'])
    session['data'] = request.form
    return redirect('/html')

@app.route('/')
def run_html():
    return render_template('index.html')

@app.route('/html')
def post_post():
    return render_template('post_post.html')

@app.route('/clear')
def clear():
    print('clear works')
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)