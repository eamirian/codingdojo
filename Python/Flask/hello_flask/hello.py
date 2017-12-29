from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/success')
def success():
  return render_template('success.html')

@app.route('/')
def hello_world():
  return render_template("index.html", name="Edwin")
  
app.run(debug=True)                       # Run the app in debug mode.
