from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'dojo'  # Return the string 'Dojo

@app.route('/say/<name>')
def greeting(name):
    return f"Hi {name}"  # Return the f string Hi and a name var

@app.route('/repeat/<name>/<int:num>')
def repeat(name, num):
    return f"Hi {name * num}"  # Return the f string Hi and a name var

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.