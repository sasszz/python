from flask import Flask, render_template


app = Flask(__name__)    # Create a new instance of the Flask class called 'app'

@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<int:num>')
def multipleboxes(num):
    return render_template("numboxes.html", num = num)

@app.route('/play/<int:num>/<string:color>')
def colorboxes(num, color):
    return render_template("colorboxes.html", num = num, color = color)

if __name__=='__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode