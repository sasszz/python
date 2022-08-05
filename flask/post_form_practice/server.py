from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/html')

@app.route('/')
def run_html():
    return render_template('index.html')

@app.route('/html')
def post_post():
    return render_template('post_post.html')


if __name__=='__main__':
    app.run(debug=True)